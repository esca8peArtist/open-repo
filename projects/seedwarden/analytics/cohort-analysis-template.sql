-- =============================================================================
-- Seedwarden Cohort Analysis SQL Template
-- =============================================================================
-- Purpose: Etsy API data transformations + cohort queries for growth analysis.
-- Data source: Etsy Open API v3 — receipts, transactions, listings endpoints.
-- Setup: Load Etsy API exports into a local SQLite or DuckDB file, or run
--        against a Postgres schema if you have a lightweight ETL pipeline.
--
-- Tables assumed:
--   orders        — one row per Etsy order/receipt
--   order_items   — one row per line item within an order
--   products      — product reference table (price, category, bundle flag)
--   email_subs    — Kit (ConvertKit) subscriber export (subscriber_id, email,
--                   subscribed_at, tags, last_open, open_count, total_sends)
--   email_clicks  — Kit click event export (subscriber_id, send_id, link_url,
--                   clicked_at, tag_applied)
--
-- All monetary values in USD. All timestamps in UTC.
-- =============================================================================


-- =============================================================================
-- SECTION 1: RAW DATA STAGING VIEWS
-- =============================================================================

-- 1.1  Enrich orders with derived fields used throughout later queries
CREATE OR REPLACE VIEW v_orders_enriched AS
SELECT
    o.order_id,
    o.buyer_email,
    o.order_date,
    o.gross_revenue,
    -- Etsy fee approximation: 6.5% transaction + 3% + $0.25 payment processing
    ROUND(o.gross_revenue * 0.095 + 0.25, 2)                      AS etsy_fees,
    ROUND(o.gross_revenue - (o.gross_revenue * 0.095 + 0.25), 2)  AS net_revenue,
    o.channel,         -- 'etsy_organic' | 'etsy_ads' | 'email_utm' | 'pinterest_utm' | 'influencer_code'
    o.coupon_code,
    o.buyer_country,
    -- Season of acquisition
    CASE
        WHEN EXTRACT(MONTH FROM o.order_date) IN (1, 2, 3, 4)   THEN 'spring_planning'
        WHEN EXTRACT(MONTH FROM o.order_date) IN (5, 6)         THEN 'long_tail_spring'
        WHEN EXTRACT(MONTH FROM o.order_date) IN (7, 8, 9)      THEN 'preservation'
        WHEN EXTRACT(MONTH FROM o.order_date) IN (10)           THEN 'long_tail_fall'
        WHEN EXTRACT(MONTH FROM o.order_date) IN (11, 12)       THEN 'holiday_gift'
        ELSE 'unknown'
    END AS acquisition_season,
    -- Calendar year-month for bucketing
    TO_CHAR(o.order_date, 'YYYY-MM')                              AS order_ym,
    -- Cohort month = first order month per buyer (joined below)
    fc.cohort_ym,
    fc.first_order_id,
    fc.first_product_id,
    fc.first_product_price_tier,
    -- Months since first purchase (for LTV curve)
    (EXTRACT(YEAR FROM o.order_date) - EXTRACT(YEAR FROM fc.first_order_date)) * 12
    + (EXTRACT(MONTH FROM o.order_date) - EXTRACT(MONTH FROM fc.first_order_date))
                                                                  AS months_since_first_purchase
FROM orders o
JOIN (
    -- First order per buyer
    SELECT
        buyer_email,
        MIN(order_date)                                   AS first_order_date,
        MIN(order_id)                                     AS first_order_id,
        TO_CHAR(MIN(order_date), 'YYYY-MM')               AS cohort_ym,
        -- First product purchased (lowest order_item_id as proxy for first item)
        FIRST_VALUE(oi.product_id) OVER (
            PARTITION BY o2.buyer_email
            ORDER BY o2.order_date, oi.order_item_id
        )                                                 AS first_product_id,
        -- Price tier of first product
        CASE
            WHEN p.price BETWEEN 0  AND 9.99  THEN 'entry'
            WHEN p.price BETWEEN 10 AND 15.99 THEN 'mid'
            WHEN p.price BETWEEN 16 AND 29.99 THEN 'premium'
            WHEN p.price >= 30               THEN 'bundle'
        END                                               AS first_product_price_tier
    FROM orders o2
    JOIN order_items oi  ON oi.order_id  = o2.order_id
    JOIN products p      ON p.product_id = oi.product_id
    GROUP BY o2.buyer_email
) fc ON fc.buyer_email = o.buyer_email;


-- =============================================================================
-- SECTION 2: COHORT RETENTION TABLE
-- =============================================================================

-- 2.1  Monthly retention — what percentage of each cohort made a purchase
--      in month N after their acquisition month?
--      This is the standard SaaS cohort retention table adapted for e-commerce.

CREATE OR REPLACE VIEW v_cohort_retention AS
SELECT
    cohort_ym,
    months_since_first_purchase                                       AS month_number,
    COUNT(DISTINCT buyer_email)                                       AS active_buyers,
    -- Cohort size = buyers acquired in cohort_ym
    cohort_sizes.cohort_size,
    ROUND(
        100.0 * COUNT(DISTINCT buyer_email) / cohort_sizes.cohort_size,
        1
    )                                                                 AS retention_pct
FROM v_orders_enriched oe
JOIN (
    SELECT cohort_ym, COUNT(DISTINCT buyer_email) AS cohort_size
    FROM v_orders_enriched
    WHERE months_since_first_purchase = 0
    GROUP BY cohort_ym
) cohort_sizes USING (cohort_ym)
GROUP BY cohort_ym, months_since_first_purchase, cohort_sizes.cohort_size
ORDER BY cohort_ym, month_number;

-- Expected output shape (run this query monthly):
--  cohort_ym | month_number | active_buyers | cohort_size | retention_pct
--  2026-05   | 0            | 12            | 12          | 100.0
--  2026-05   | 1            | 2             | 12          | 16.7
--  2026-05   | 3            | 3             | 12          | 25.0
--  2026-06   | 0            | 8             | 8           | 100.0
--  ...


-- =============================================================================
-- SECTION 3: LTV CURVES BY COHORT
-- =============================================================================

-- 3.1  Cumulative net revenue per buyer by months since first purchase
--      Use this to build the LTV curves plotted in dashboard-template.ipynb.

CREATE OR REPLACE VIEW v_ltv_by_cohort AS
SELECT
    cohort_ym,
    months_since_first_purchase                             AS month_number,
    COUNT(DISTINCT buyer_email)                             AS buyers_with_any_purchase,
    SUM(net_revenue)                                        AS cohort_revenue_in_month,
    -- Cumulative revenue per original cohort size
    SUM(SUM(net_revenue)) OVER (
        PARTITION BY cohort_ym
        ORDER BY months_since_first_purchase
    ) / MAX(cohort_sizes.cohort_size)                       AS cumulative_ltv_per_buyer
FROM v_orders_enriched oe
JOIN (
    SELECT cohort_ym, COUNT(DISTINCT buyer_email) AS cohort_size
    FROM v_orders_enriched WHERE months_since_first_purchase = 0
    GROUP BY cohort_ym
) cohort_sizes USING (cohort_ym)
GROUP BY cohort_ym, months_since_first_purchase, cohort_sizes.cohort_size
ORDER BY cohort_ym, month_number;


-- 3.2  LTV by first-product price tier (entry / mid / premium / bundle)
--      Aggregated across all cohorts — use once you have 6+ months of data.

SELECT
    first_product_price_tier,
    COUNT(DISTINCT buyer_email)                                     AS total_buyers,
    AVG(total_net_revenue)                                          AS avg_ltv,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_net_revenue)  AS median_ltv,
    AVG(purchase_count)                                             AS avg_purchase_count
FROM (
    SELECT
        buyer_email,
        first_product_price_tier,
        SUM(net_revenue)   AS total_net_revenue,
        COUNT(order_id)    AS purchase_count
    FROM v_orders_enriched
    GROUP BY buyer_email, first_product_price_tier
) buyer_summary
GROUP BY first_product_price_tier
ORDER BY avg_ltv DESC;


-- =============================================================================
-- SECTION 4: SEASONAL COHORT ANALYSIS
-- =============================================================================

-- 4.1  Revenue contribution by seasonal acquisition cohort and calendar month
--      Answers: do Spring Planning buyers spend in preservation season? etc.

SELECT
    acquisition_season,
    order_ym                                AS revenue_month,
    COUNT(DISTINCT buyer_email)             AS active_buyers,
    SUM(net_revenue)                        AS total_net_revenue,
    AVG(net_revenue)                        AS avg_order_value,
    COUNT(order_id)                         AS order_count
FROM v_orders_enriched
GROUP BY acquisition_season, order_ym
ORDER BY acquisition_season, order_ym;


-- 4.2  Second-purchase rate by seasonal acquisition cohort
--      Key metric: which cohort has the best 90-day repeat rate?

SELECT
    acquisition_season,
    COUNT(DISTINCT buyer_email)                                     AS cohort_size,
    COUNT(DISTINCT CASE WHEN purchase_rank = 2 THEN buyer_email END) AS second_purchase_buyers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN purchase_rank = 2 THEN buyer_email END)
        / COUNT(DISTINCT buyer_email),
        1
    )                                                               AS second_purchase_rate_pct,
    -- 90-day second-purchase rate specifically
    COUNT(DISTINCT CASE
        WHEN purchase_rank = 2
         AND months_since_first_purchase <= 3
        THEN buyer_email
    END)                                                            AS second_purchase_within_90d,
    ROUND(
        100.0 * COUNT(DISTINCT CASE
            WHEN purchase_rank = 2
             AND months_since_first_purchase <= 3
            THEN buyer_email
        END) / COUNT(DISTINCT buyer_email),
        1
    )                                                               AS second_purchase_90d_rate_pct
FROM (
    SELECT
        oe.*,
        ROW_NUMBER() OVER (
            PARTITION BY buyer_email
            ORDER BY order_date
        ) AS purchase_rank
    FROM v_orders_enriched oe
) ranked
GROUP BY acquisition_season
ORDER BY second_purchase_rate_pct DESC;


-- =============================================================================
-- SECTION 5: PRODUCT-LEVEL COHORT ANALYSIS
-- =============================================================================

-- 5.1  Repeat-purchase trigger rate by first product
--      Which product as "first purchase" leads most reliably to a second?

SELECT
    p.product_name,
    p.price,
    p.is_bundle,
    COUNT(DISTINCT oe.buyer_email)                                       AS first_purchase_buyers,
    COUNT(DISTINCT CASE WHEN oe2.order_id IS NOT NULL
                        THEN oe.buyer_email END)                         AS repeat_buyers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN oe2.order_id IS NOT NULL
                                    THEN oe.buyer_email END)
        / NULLIF(COUNT(DISTINCT oe.buyer_email), 0),
        1
    )                                                                    AS repeat_purchase_trigger_rate_pct,
    -- Average days to second purchase
    AVG(CASE WHEN oe2.order_id IS NOT NULL
             THEN EXTRACT(DAY FROM oe2.order_date - oe.order_date) END)  AS avg_days_to_second_purchase
FROM v_orders_enriched oe
JOIN products p ON p.product_id = oe.first_product_id
-- Self-join to find any subsequent order by same buyer
LEFT JOIN orders oe2
    ON  oe2.buyer_email = oe.buyer_email
    AND oe2.order_id   != oe.first_order_id
    AND oe2.order_date  > oe.order_date
WHERE oe.months_since_first_purchase = 0   -- only first-purchase rows
GROUP BY p.product_name, p.price, p.is_bundle
ORDER BY repeat_purchase_trigger_rate_pct DESC;


-- 5.2  Cross-sell flow: what do buyers purchase second after each first product?

SELECT
    p1.product_name        AS first_product,
    p2.product_name        AS second_product,
    COUNT(*)               AS buyer_count,
    AVG(oe2.net_revenue)   AS avg_second_order_value
FROM (
    -- First purchase per buyer
    SELECT buyer_email, first_product_id, order_date AS first_date
    FROM v_orders_enriched
    WHERE months_since_first_purchase = 0
) fp
-- Second purchase
JOIN orders o2 ON o2.buyer_email = fp.buyer_email
              AND o2.order_date > fp.first_date
JOIN order_items oi2 ON oi2.order_id = o2.order_id
JOIN (
    -- Deduplicate to only the earliest second order per buyer
    SELECT buyer_email, MIN(order_date) AS second_date
    FROM orders
    WHERE order_id NOT IN (
        SELECT MIN(order_id) FROM orders GROUP BY buyer_email
    )
    GROUP BY buyer_email
) sd ON sd.buyer_email = fp.buyer_email AND sd.second_date = o2.order_date
JOIN orders oe2_base ON oe2_base.order_id = o2.order_id
-- Enrich net revenue
JOIN v_orders_enriched oe2 ON oe2.order_id = o2.order_id
JOIN products p1 ON p1.product_id = fp.first_product_id
JOIN products p2 ON p2.product_id = oi2.product_id
GROUP BY p1.product_name, p2.product_name
ORDER BY buyer_count DESC
LIMIT 30;


-- 5.3  Listing conversion rate by product (views to purchases)
--      Requires Etsy listing stats export with view counts.

SELECT
    p.product_name,
    p.price,
    p.is_bundle,
    ls.total_views,
    COUNT(oi.order_item_id)                         AS total_purchases,
    ROUND(
        100.0 * COUNT(oi.order_item_id) / NULLIF(ls.total_views, 0),
        2
    )                                               AS conversion_rate_pct,
    -- Flag underperformers
    CASE
        WHEN ls.total_views >= 100
         AND COUNT(oi.order_item_id) * 100.0 / NULLIF(ls.total_views, 0) < 1.0
        THEN 'NEEDS_LISTING_FIX'
        WHEN ls.total_views >= 100
         AND COUNT(oi.order_item_id) * 100.0 / NULLIF(ls.total_views, 0) >= 3.0
        THEN 'AD_CANDIDATE'
        ELSE 'NORMAL'
    END                                             AS listing_health
FROM products p
LEFT JOIN listing_stats ls ON ls.product_id = p.product_id
LEFT JOIN order_items oi   ON oi.product_id = p.product_id
GROUP BY p.product_name, p.price, p.is_bundle, ls.total_views
ORDER BY conversion_rate_pct DESC NULLS LAST;


-- =============================================================================
-- SECTION 6: EMAIL ENGAGEMENT COHORT ANALYSIS
-- =============================================================================

-- 6.1  Subscriber health distribution (engaged / marginal / cold)

SELECT
    health_tier,
    COUNT(*)                         AS subscriber_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_of_list
FROM (
    SELECT
        subscriber_id,
        CASE
            WHEN total_sends = 0
                THEN 'no_sends_yet'
            WHEN CAST(open_count AS FLOAT) / total_sends >= 0.30
                THEN 'engaged'
            WHEN CAST(open_count AS FLOAT) / total_sends >= 0.15
                THEN 'marginal'
            ELSE 'cold'
        END AS health_tier
    FROM email_subs
    WHERE subscribed_at >= CURRENT_DATE - INTERVAL '180 days'  -- active window
) health_buckets
GROUP BY health_tier
ORDER BY subscriber_count DESC;


-- 6.2  Behavioral tag segment performance (open rate, CTR, purchase rate)

SELECT
    t.tag_name,
    COUNT(DISTINCT es.subscriber_id)                             AS subscribers_with_tag,
    ROUND(
        100.0 * SUM(es.open_count) / NULLIF(SUM(es.total_sends), 0),
        1
    )                                                            AS avg_open_rate_pct,
    -- Purchase rate: subscribers with tag who also appear in orders
    COUNT(DISTINCT CASE WHEN o.buyer_email IS NOT NULL
                        THEN es.subscriber_id END)               AS purchasers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN o.buyer_email IS NOT NULL
                                    THEN es.subscriber_id END)
        / NULLIF(COUNT(DISTINCT es.subscriber_id), 0),
        1
    )                                                            AS purchase_rate_pct
FROM email_subs es
-- Tags table: one row per subscriber-tag pair
JOIN subscriber_tags t ON t.subscriber_id = es.subscriber_id
-- Link to orders via email (Kit stores subscriber email)
LEFT JOIN orders o ON o.buyer_email = es.email
GROUP BY t.tag_name
ORDER BY purchase_rate_pct DESC;


-- 6.3  Unsubscribe timing analysis
--      Which email in the welcome sequence loses the most subscribers?

SELECT
    send_sequence_position,   -- 1-5 for welcome sequence emails
    COUNT(*)                  AS unsubs_at_this_position,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        1
    )                         AS pct_of_total_unsubs
FROM email_unsub_events
WHERE automation_name = 'welcome_sequence'
GROUP BY send_sequence_position
ORDER BY send_sequence_position;


-- 6.4  Email-to-purchase funnel: open → click → purchase (by send campaign)

SELECT
    ec.campaign_name,
    ec.send_date,
    ec.total_sends,
    ec.total_opens,
    ec.total_clicks,
    COUNT(DISTINCT o.order_id)               AS purchases_within_7d,
    ROUND(100.0 * ec.total_opens  / NULLIF(ec.total_sends, 0), 1)   AS open_rate_pct,
    ROUND(100.0 * ec.total_clicks / NULLIF(ec.total_opens, 0), 1)   AS ctor_pct,
    ROUND(100.0 * COUNT(DISTINCT o.order_id) / NULLIF(ec.total_sends, 0), 2) AS send_to_purchase_pct
FROM email_campaigns ec
LEFT JOIN email_clicks eck
    ON eck.send_id   = ec.campaign_id
    AND eck.clicked_at BETWEEN ec.send_date AND ec.send_date + INTERVAL '7 days'
LEFT JOIN orders o
    ON  o.buyer_email = (SELECT email FROM email_subs WHERE subscriber_id = eck.subscriber_id)
    AND o.order_date  BETWEEN ec.send_date AND ec.send_date + INTERVAL '7 days'
GROUP BY ec.campaign_name, ec.send_date, ec.total_sends, ec.total_opens, ec.total_clicks
ORDER BY ec.send_date DESC;


-- =============================================================================
-- SECTION 7: CAC AND PAYBACK PERIOD CALCULATIONS
-- =============================================================================

-- 7.1  CAC by acquisition channel (requires ad spend table)

SELECT
    channel,
    COUNT(DISTINCT buyer_email)                                  AS customers_acquired,
    SUM(channel_spend.spend)                                     AS total_spend,
    ROUND(
        SUM(channel_spend.spend) / NULLIF(COUNT(DISTINCT buyer_email), 0),
        2
    )                                                            AS cac,
    ROUND(AVG(oe.net_revenue), 2)                                AS avg_first_order_net_revenue,
    -- Payback: months until cumulative net revenue per buyer exceeds CAC
    -- Simplified: if first-order net revenue > CAC, payback = 0 months (same transaction)
    CASE
        WHEN AVG(oe.net_revenue) >=
             SUM(channel_spend.spend) / NULLIF(COUNT(DISTINCT buyer_email), 0)
        THEN 0
        ELSE NULL  -- requires LTV curve to compute; see v_ltv_by_cohort
    END                                                          AS first_transaction_payback_months
FROM v_orders_enriched oe
-- Channel spend table: manually populated from Etsy ads dashboard,
-- Pinterest ads, and Facebook/Instagram ads exports
JOIN channel_spend ON channel_spend.channel = oe.channel
                   AND channel_spend.spend_month = oe.order_ym
WHERE oe.months_since_first_purchase = 0
GROUP BY oe.channel
ORDER BY cac;


-- 7.2  ROAS by paid channel (weekly)

SELECT
    channel,
    spend_week,
    SUM(gross_revenue)                                           AS gross_revenue,
    SUM(channel_spend.spend)                                     AS ad_spend,
    ROUND(SUM(gross_revenue) / NULLIF(SUM(channel_spend.spend), 0), 2) AS roas,
    CASE
        WHEN ROUND(SUM(gross_revenue) / NULLIF(SUM(channel_spend.spend), 0), 2) >= 2.5
        THEN 'SCALE'
        WHEN ROUND(SUM(gross_revenue) / NULLIF(SUM(channel_spend.spend), 0), 2) BETWEEN 1.5 AND 2.49
        THEN 'MAINTAIN'
        ELSE 'PAUSE_AND_FIX'
    END                                                          AS roas_action
FROM v_orders_enriched oe
JOIN channel_spend ON channel_spend.channel = oe.channel
                   AND DATE_TRUNC('week', channel_spend.spend_date) = DATE_TRUNC('week', oe.order_date)
WHERE oe.channel IN ('etsy_ads', 'pinterest_utm', 'facebook_utm')
GROUP BY oe.channel, DATE_TRUNC('week', oe.order_date)
ORDER BY spend_week DESC, roas DESC;


-- =============================================================================
-- SECTION 8: MONTHLY EXECUTIVE SUMMARY QUERY
-- =============================================================================
-- Run this once per month to populate the monthly metrics checklist.

SELECT
    -- Revenue
    TO_CHAR(CURRENT_DATE, 'YYYY-MM')                             AS reporting_month,
    SUM(net_revenue)                                             AS mtd_net_revenue,
    COUNT(DISTINCT order_id)                                     AS mtd_orders,
    ROUND(SUM(net_revenue) / NULLIF(COUNT(DISTINCT order_id), 0), 2) AS avg_order_value,
    -- Cohort health
    COUNT(DISTINCT buyer_email)                                  AS unique_buyers_mtd,
    COUNT(DISTINCT CASE WHEN months_since_first_purchase > 0
                        THEN buyer_email END)                    AS repeat_buyers_mtd,
    ROUND(
        100.0 * COUNT(DISTINCT CASE WHEN months_since_first_purchase > 0
                                    THEN buyer_email END)
        / NULLIF(COUNT(DISTINCT buyer_email), 0),
        1
    )                                                            AS repeat_buyer_rate_pct,
    -- Seasonal context
    acquisition_season,
    -- Bundle vs. individual mix
    ROUND(
        100.0 * SUM(CASE WHEN p.is_bundle THEN net_revenue ELSE 0 END)
        / NULLIF(SUM(net_revenue), 0),
        1
    )                                                            AS bundle_revenue_pct
FROM v_orders_enriched oe
JOIN order_items oi ON oi.order_id = oe.order_id
JOIN products p     ON p.product_id = oi.product_id
WHERE order_ym = TO_CHAR(CURRENT_DATE, 'YYYY-MM')
GROUP BY acquisition_season;


-- =============================================================================
-- APPENDIX: TABLE SCHEMAS (for local SQLite / DuckDB setup)
-- =============================================================================

/*
CREATE TABLE orders (
    order_id        TEXT PRIMARY KEY,
    buyer_email     TEXT NOT NULL,
    order_date      TIMESTAMP NOT NULL,
    gross_revenue   NUMERIC(8,2) NOT NULL,
    channel         TEXT,        -- 'etsy_organic' | 'etsy_ads' | 'email_utm' | etc.
    coupon_code     TEXT,
    buyer_country   TEXT,
    etsy_receipt_id TEXT
);

CREATE TABLE order_items (
    order_item_id   TEXT PRIMARY KEY,
    order_id        TEXT NOT NULL REFERENCES orders(order_id),
    product_id      TEXT NOT NULL,
    quantity        INTEGER DEFAULT 1,
    unit_price      NUMERIC(8,2)
);

CREATE TABLE products (
    product_id      TEXT PRIMARY KEY,
    product_name    TEXT NOT NULL,
    price           NUMERIC(8,2),
    is_bundle       BOOLEAN DEFAULT FALSE,
    category        TEXT,   -- 'planning' | 'preservation' | 'sovereignty' | 'homesteading'
    seasonal_peak   TEXT    -- 'spring' | 'preservation' | 'holiday' | 'year_round'
);

CREATE TABLE listing_stats (
    product_id      TEXT REFERENCES products(product_id),
    stat_date       DATE,
    total_views     INTEGER,
    total_favorites INTEGER,
    PRIMARY KEY (product_id, stat_date)
);

CREATE TABLE email_subs (
    subscriber_id   TEXT PRIMARY KEY,
    email           TEXT NOT NULL UNIQUE,
    subscribed_at   TIMESTAMP,
    tags            TEXT,   -- comma-separated Kit tags
    last_open       TIMESTAMP,
    open_count      INTEGER DEFAULT 0,
    total_sends     INTEGER DEFAULT 0,
    is_active       BOOLEAN DEFAULT TRUE
);

CREATE TABLE subscriber_tags (
    subscriber_id   TEXT REFERENCES email_subs(subscriber_id),
    tag_name        TEXT,
    applied_at      TIMESTAMP,
    PRIMARY KEY (subscriber_id, tag_name)
);

CREATE TABLE email_campaigns (
    campaign_id     TEXT PRIMARY KEY,
    campaign_name   TEXT,
    automation_name TEXT,   -- 'welcome_sequence' | 'newsletter' | 'broadcast' | etc.
    send_sequence_position INTEGER,
    send_date       TIMESTAMP,
    total_sends     INTEGER,
    total_opens     INTEGER,
    total_clicks    INTEGER
);

CREATE TABLE email_clicks (
    click_id        TEXT PRIMARY KEY,
    send_id         TEXT REFERENCES email_campaigns(campaign_id),
    subscriber_id   TEXT REFERENCES email_subs(subscriber_id),
    link_url        TEXT,
    clicked_at      TIMESTAMP,
    tag_applied     TEXT
);

CREATE TABLE email_unsub_events (
    unsub_id        TEXT PRIMARY KEY,
    subscriber_id   TEXT,
    automation_name TEXT,
    send_sequence_position INTEGER,
    unsubbed_at     TIMESTAMP
);

CREATE TABLE channel_spend (
    spend_id        TEXT PRIMARY KEY,
    channel         TEXT,
    spend_date      DATE,
    spend_month     TEXT,   -- 'YYYY-MM'
    spend_week      DATE,   -- Monday of the week
    spend           NUMERIC(8,2)
);
*/

-- End of cohort-analysis-template.sql
