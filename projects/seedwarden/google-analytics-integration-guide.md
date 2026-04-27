# Google Analytics 4 Integration Guide for Seedwarden

**Purpose**: Track customer behavior on Seedwarden product pages and website to segment customers by cohort (forager, prepper, homesteader, gift buyer).

**Setup time**: 30–60 minutes (one-time)
**Maintenance**: 10 minutes/week (log in, review segments)

---

## Step 1: Set Up Google Analytics 4 Property

1. Go to [analytics.google.com](https://analytics.google.com)
2. Click **Create** (or add a new property to existing GA account)
3. Property name: `Seedwarden`
4. Property timezone: `US/Eastern` (or your current timezone)
5. Industry category: `Retail`
6. Business objectives: Check `Purchase`, `Lead generation` (if applicable)

**Tracking ID**: You'll receive a Measurement ID like `G-XXXXXXXXXX`. Save this.

---

## Step 2: Install GA4 Tracking Code

### Option A: If Seedwarden has its own website

Add this code to the `<head>` section of every page:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with your actual Measurement ID.

### Option B: If selling via Etsy listings (no custom website)

You cannot install GA4 directly on Etsy listings. Instead, use **UTM parameters** to track traffic flow:

When you link to Etsy listings from external sources (Pinterest, blogs, email), append UTM parameters:

```
https://www.etsy.com/listing/[LISTING_ID]?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]
```

**Examples**:
- Pinterest traffic: `?utm_source=pinterest&utm_medium=organic&utm_campaign=forager_spring`
- Email campaign: `?utm_source=email&utm_medium=newsletter&utm_campaign=may_update`
- Reddit post: `?utm_source=reddit&utm_medium=r_foraging&utm_campaign=organic`
- Homesteading blog: `?utm_source=backwoods_home&utm_medium=blog&utm_campaign=guest_post`

GA4 will track these as traffic sources and campaigns, helping segment visitors.

---

## Step 3: Create Custom Events

Custom events help identify cohort behavior. Add these events to your tracking code:

### Event: "View Edible Guides"
Fire when user views any "wild edibles" or "medicinal plants" guide page

```javascript
gtag('event', 'view_edible_guides', {
  'guide_type': 'wild_edibles',
  'guide_name': 'Wild Edibles Guide',
  'page_path': window.location.pathname
});
```

### Event: "View Prepper Content"
Fire when user views "survival prep" or "emergency" content

```javascript
gtag('event', 'view_prepper_content', {
  'content_type': 'survival_guide',
  'content_name': 'Complete Bundle',
  'page_path': window.location.pathname
});
```

### Event: "View Medicinal Content"
Fire when user views medicinal plants or homesteading guides

```javascript
gtag('event', 'view_medicinal_content', {
  'content_type': 'medicinal_guide',
  'content_name': 'Medicinal Plants',
  'page_path': window.location.pathname
});
```

### Event: "High Engagement"
Fire if user spends >3 minutes on a page (indicator of serious interest)

```javascript
setTimeout(function() {
  gtag('event', 'high_engagement', {
    'engagement_type': 'long_session',
    'page_path': window.location.pathname,
    'time_on_page': 180
  });
}, 180000); // 3 minutes
```

---

## Step 4: Create Audience Segments

Go to **Admin** > **Audience Definition** > **Create Audience** to segment visitors by behavior:

### Segment 1: Forager Segment
**Condition**: Users who viewed "wild edibles" or "medicinal plants" pages + spent >2 min

- Event: `view_edible_guides` OR `view_medicinal_content`
- Session duration: > 120 seconds
- **Purpose**: Identify foragers for seasonal messaging

### Segment 2: Prepper Segment
**Condition**: Users who viewed prepper/survival content

- Event: `view_prepper_content`
- Any traffic source
- **Purpose**: Identify preppers for event-driven campaigns

### Segment 3: Homesteader Segment
**Condition**: Users who viewed both medicinal AND product pages

- Event: `view_medicinal_content` AND viewed product page
- **Purpose**: Identify homesteaders for year-round campaigns

### Segment 4: Gift Buyers
**Condition**: Mobile traffic + short session duration + viewed during gift-giving seasons (May, Nov–Dec)

- Device: Mobile
- Session duration: < 60 seconds
- Traffic source: Pinterest, Instagram, Etsy
- Date range: May 1–10, Nov 1–Dec 31
- **Purpose**: Identify gift buyers for seasonal promotions

---

## Step 5: Set Up Goal Tracking

Goals = conversions you want to track (e.g., purchases, newsletter signups, downloads).

Go to **Admin** > **Goals** and create:

### Goal 1: Purchase Completion
**Type**: Event
**Event name**: `purchase`
**Condition**: Order value > $0

### Goal 2: Newsletter Signup
**Type**: Event
**Event name**: `newsletter_signup`

### Goal 3: Engaged Users
**Type**: Duration
**Condition**: Session duration > 3 minutes

---

## Step 6: Link Etsy Orders Back to GA (Optional but Recommended)

If you have email addresses for Etsy customers, you can:

1. Export Etsy customer email list (via Etsy Dashboard)
2. Create a list in GA4 > **Audiences** > **Customer Lists**
3. Match emails to GA4 visitors
4. This shows which email addresses converted

**Process**:
- Etsy exports: `ORD-001` customer → email → name
- GA4 User-ID tracking: Set `user_id` = customer email in GA code
- GA4 then associates visits with that customer's email

This requires adding to your GA tracking code:

```javascript
gtag('config', 'G-XXXXXXXXXX', {
  'user_id': 'customer_email@example.com'
});
```

---

## Step 7: Monthly Reporting Dashboard

Create a monthly view of key metrics:

1. Go to **Reports** > **Realtime** (see live traffic)
2. Create a custom report:
   - **Rows**: Traffic source, campaign, event name
   - **Values**: Users, sessions, events, conversion rate
   - **Filter**: Date range (monthly)

**Export to spreadsheet** (click the spreadsheet icon) and update `etsy-analytics-template.csv` with:
- Total visits
- Conversion rate (purchases / visits)
- Traffic source breakdown
- Top pages by cohort

---

## Step 8: Link Cohort Segment to Email Campaigns

Once you've identified cohort segments in GA4:

1. Create a list export in GA4 (Users in "Forager Segment")
2. Export as `.csv`
3. Upload to email platform (Mailchimp, Klaviyo) as a segment
4. Send cohort-specific emails:
   - Foragers: Seasonal guides (spring mushrooms, fall nuts)
   - Preppers: Event-driven (news of economic uncertainty)
   - Homesteaders: Project-based (spring planting, fall preservation)
   - Gift buyers: Holiday campaigns (May, Nov–Dec)

---

## Troubleshooting

**Q: GA4 shows 0 events even though I have traffic**
- A: Check that tracking code is installed correctly in `<head>` section
- Verify Measurement ID is correct (starts with `G-`)
- Wait 24–48 hours for GA4 to process initial data

**Q: Events aren't firing**
- A: Check browser console (F12) for JavaScript errors
- Verify event names match exactly (case-sensitive)
- Test with GA4 DebugView: Add `&debug_mode=true` to URL, then check reports in real-time

**Q: Etsy traffic doesn't show in GA4**
- A: You cannot track Etsy traffic directly (Etsy blocks external GA tracking)
- Use UTM parameters on links TO Etsy instead
- Track only traffic to your own website (if you have one)

**Q: How do I see which customers are in each cohort?**
- A: GA4 doesn't show individual customer names by default
- Instead, use audience segments + email list matching (see Step 6)
- Or manually tag customers in `customer-analytics.csv` based on survey responses

---

## Monthly Maintenance Checklist

- [ ] **Week 1**: Pull GA4 report; update `etsy-analytics-template.csv`
- [ ] **Week 2**: Compare to Etsy Dashboard metrics (validation)
- [ ] **Week 3**: Check segment traffic (forager vs. prepper ratio)
- [ ] **Week 4**: Export cohort audience lists; update email platform segments

---

## Cost

GA4 is **free** for up to 10 million events per month (Phase 1 won't exceed this).

Paid features (unnecessary for Phase 1):
- Google 4 Ads integration (for retargeting): Optional, free
- BigQuery export: Free tier includes 1GB/month

---

## Next Steps

1. Install GA4 and let it collect data for 2 weeks
2. Review traffic sources in **Reports** > **Traffic acquisition**
3. Create first audience segment (Foragers)
4. Compare GA4 data to Etsy Dashboard to validate
5. Adjust segment definitions based on actual traffic patterns

---

**Questions?** Refer to [GA4 documentation](https://support.google.com/analytics/answer/10089681) or the `customer-cohort-analysis-framework.md` for more context on cohort definitions.

