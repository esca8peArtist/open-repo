---
title: AI Inference Node — Hardware Options
created: 2026-05-13
status: research-complete
budget_target: $3500
budget_hard_cap: $6000
use_case: always-on local 70B+ inference server
tags: [hardware, AI, inference, local-llm, shopping]
---

# AI Inference Node — Hardware Options

> **Research date:** May 2026. Prices are current market rates; GPU prices remain elevated and volatile due to AI-driven demand and ongoing supply constraints.

---

## Summary Comparison Table

| Build | Total Cost | VRAM/UMem | 70B Q4 Tok/s | Max Model (Q4) | Idle W | Peak W | 3yr Elec. Cost | Verdict |
|---|---|---|---|---|---|---|---|---|
| **Mac Studio M4 Max 128GB** | $3,699 | 128GB unified | ~15–18 | ~110B Q4 | ~7W | ~80W | ~$95 | Best all-rounder for budget; excellent efficiency |
| **Mac Studio M3 Ultra 192GB** | $6,999+ | 192GB unified | ~25–30 | ~160B Q4 | ~8W | ~180W | ~$240 | Exceeds budget; best Apple Silicon performance |
| **Dual RTX 4090 (PCIe)** | ~$5,200–$6,000 | 48GB GDDR6X | ~20–24 | ~40B Q4 fit; 70B split | ~100W sys | ~950W | ~$1,250 | High TCO; best CUDA throughput in budget |
| **Single RTX 5090** | ~$3,700–$5,500 | 32GB GDDR7 | ~35–45 | ~24B Q4 fit; 70B partial offload | ~60W sys | ~600W | ~$790 | Scarce & overpriced; 70B offload still needed |
| **RTX A6000 48GB (used)** | ~$3,500–$4,500 | 48GB GDDR6 | ~18–22 | ~40B Q4; 70B marginal | ~80W sys | ~380W | ~$500 | Good VRAM density; older Ampere arch; quiet |
| **Dual RX 7900 XTX** | ~$2,800–$3,400 | 48GB GDDR6 | ~12–16 | ~40B Q4 | ~90W sys | ~650W | ~$855 | Cheapest 48GB option; ROCm is still maturing |
| **RX 9070 XT (single)** | ~$700–$900 | 16GB GDDR6 | ~18–22 on 13B | Cannot do 70B | ~50W sys | ~220W | ~$290 | Wrong tier for 70B; fine for 32B |
| **Refurb Workstation + A100 80GB PCIe** | ~$6,000–$8,000 | 80GB HBM2e | ~30–40 | ~70B Q8 comfortably | ~150W sys | ~500W | ~$660 | Exceeds budget; enterprise-grade reliability |

**Recommended pick at budget:** Mac Studio M4 Max 128GB ($3,699). Best balance of cost, efficiency, 70B capability, and zero-friction software stack.

**Best performance under $6k:** Dual RTX 4090 build (~$5,400), but pay attention to the 3-year electricity cost — it nearly wipes out the price advantage vs. Mac Studio over time.

---

## Detailed Profiles

---

### 1. Apple Mac Studio M4 Max — 128GB

**Verdict: Best value pick. The recommended option for this use case.**

The current Mac Studio (released March 2025) ships with either the M4 Max or M3 Ultra. Apple canceled the M4 Ultra; the next generation (M5 Max / M5 Ultra) is not expected until October 2026 at the earliest. The M4 Max at 128GB is the current sweet spot.

| Spec | Value |
|---|---|
| Total cost | $3,699 (1TB SSD config) |
| Memory | 128GB unified (Metal-shared CPU/GPU) |
| Memory bandwidth | 546 GB/s |
| GPU cores | 40-core |
| Recommended system RAM | N/A — unified memory serves both roles |
| Tokens/sec, 70B Q4 (MLX) | ~15–18 tok/s |
| Tokens/sec, 70B Q4 (llama.cpp Metal) | ~12–14 tok/s |
| Max model size (Q4) | ~110B (fits comfortably with KV cache headroom) |
| Max model size (Q8) | ~60B (tight; fits Llama 3.3 70B at Q4 or Qwen3 72B at Q4) |
| Idle power draw | ~7–8W (whole system) |
| Peak power draw | ~80W (inference workload) |
| Annual electricity @ $0.15/kWh, 24/7 idle | ~$9/yr idle; ~$105/yr at 100% load |
| 3-year electricity estimate (mixed duty) | ~$75–$200 depending on utilization |
| Thermal / noise | Virtually silent. Single small fan rarely spins up. Home-office perfect. |
| Ecosystem | Metal / MLX. Excellent. LM Studio, Ollama, llama.cpp Metal backend all well-supported. MLX is 30–50% faster than llama.cpp Metal on Apple Silicon. |

**Key weaknesses:**
- 15–18 tok/s is adequate for single-user interactive use but not fast. At this speed a 70B model generates ~1 token per 60ms — readable but perceptibly slow for long outputs.
- No CUDA. vLLM and many fine-tuning frameworks require CUDA; you are locked into llama.cpp, Ollama, and MLX-LM.
- Cannot run Q8 70B models without being very tight on KV cache. For Q8 70B (Qwen3 72B ~76GB) you are at the memory limit.
- The M4 Max has lower memory bandwidth than the M3 Ultra (546 vs 800 GB/s), which directly limits token throughput. The M3 Ultra is ~40–50% faster on 70B.
- No upgradability. VRAM is the chip.

**Add-ons needed:** None. Out-of-box capable of the use case.

---

### 2. Apple Mac Studio M3 Ultra — 192GB

**Verdict: The best Apple Silicon option but breaks the $6k hard cap at base config.**

The M3 Ultra uses two M3 Max dies connected via UltraFusion, giving 192GB unified memory and 800 GB/s bandwidth. It was released alongside the M4 Max Mac Studio in March 2025.

| Spec | Value |
|---|---|
| Total cost | $6,999 (base 192GB / 60-core GPU) — exceeds hard cap |
| Memory | 192GB unified |
| Memory bandwidth | 800 GB/s |
| GPU cores | 60-core |
| Tokens/sec, 70B Q4 (MLX) | ~25–30 tok/s |
| Tokens/sec, 70B Q4 (llama.cpp Metal) | ~18–22 tok/s |
| Max model size (Q4) | ~160B (can run Llama 3.1 405B in aggressive quant; 70B at Q8 trivially) |
| Max model size (Q8) | ~90B (comfortable) |
| Idle power draw | ~8–9W (whole system; per Tweaktown cluster test) |
| Peak power draw | ~180W |
| Annual electricity @ $0.15/kWh, 24/7 idle | ~$11/yr idle; ~$235/yr at 100% load |
| 3-year electricity estimate (mixed duty) | ~$150–$400 |
| Thermal / noise | Near-silent. Twin fans, but rarely audible under inference load. |
| Ecosystem | Same as M4 Max — Metal / MLX. |

**Key weaknesses:**
- $6,999 is the base price, already at the hard cap. Any BTO (storage) pushes it over.
- Still no CUDA. Same ecosystem limitations as M4 Max.
- The tokens/sec advantage over M4 Max is real (~65%) but the cost delta is ~89%. Performance-per-dollar favors M4 Max.
- The next Mac Studio (M5) is expected in October 2026 and will offer 30% faster CPU and presumably better bandwidth — buying M3 Ultra now means buying a platform that will be superseded in ~5 months.

**Add-ons needed:** None, but buying at this tier is hard to justify given M5 Ultra is imminent and M4 Max at 128GB is 89% cheaper.

---

### 3. Custom Build: Dual RTX 4090 (PCIe 4.0 x16/x8)

**Verdict: Highest raw CUDA throughput in budget, but terrible 24/7 power costs and significant build complexity.**

Single RTX 4090 cards can no longer be purchased new (production ended); they are used/secondary market only at ~$1,800–$2,200 each. Dual-4090 is the highest-performance CUDA path under $6k.

| Spec | Value |
|---|---|
| Total cost | 2x RTX 4090 (~$4,000–$4,400) + platform (Threadripper/HEDT or high-end ATX, 1200W+ PSU, 64GB DDR5 RAM) = **~$5,500–$6,000** |
| VRAM | 48GB total (24GB per card, no NVLink — split via llama.cpp tensor parallelism) |
| Recommended system RAM | 64–128GB DDR5 for model offload headroom |
| Tokens/sec, 70B Q4 | ~20–24 tok/s (PCIe-limited; 10–15% slower than NVLink would be) |
| Max model size (Q4 in VRAM) | ~40B (fits on 48GB combined); 70B Q4 (~40GB weights) fits with ~8GB for KV cache |
| Max model size (Q8) | ~48GB = Llama 3.3 70B Q8 is ~75GB — does not fit; requires CPU offload |
| Idle power draw | ~100–130W whole system (two GPUs at idle ~60W combined + platform ~60W) |
| Peak power draw | ~950–1000W (two GPUs at ~450W TDP each + platform) |
| Annual electricity @ $0.15/kWh, 24/7 (75% load avg) | **~$935/yr** |
| 3-year electricity cost | **~$2,800** |
| 3-year TCO (hardware + electricity) | ~$8,300–$8,800 |
| Thermal / noise | Two 450W GPUs in a consumer case = significant heat and fan noise. Not quiet. Requires good case airflow or AIO cooling. |
| Ecosystem | CUDA. Excellent. Full llama.cpp CUDA, Ollama, vLLM, exllamav2, TensorRT-LLM. Best ecosystem for fine-tuning tools too. |

**Add-ons / requirements:**
- 1200W+ 80 Plus Gold PSU: ~$150–$200
- ATX platform with two full PCIe 4.0 x16 slots (e.g., ASUS ProArt X670E, Threadripper boards): second slot runs at x8, which is adequate for inference
- Case with dual-slot GPU spacing and good airflow: $80–$150
- 64GB DDR5 RAM minimum: ~$100–$150

**Key weaknesses:**
- 70B Q4 fits in 48GB combined VRAM but the 8GB remainder for KV cache is tight. At long context windows (>16K tokens), cache spills to RAM and speed drops sharply.
- Q8 70B does NOT fit — requires CPU offload, degrading to 5–8 tok/s.
- Power costs over 3 years (~$2,800) rival or exceed the hardware cost itself at this compute level.
- Used RTX 4090 market carries risk: ex-mining cards, no warranty. Inspect carefully.
- This is a workstation, not a server — noise/thermals require a dedicated room or tolerance for fan noise.
- NVLink is not available for RTX 4090 (NVIDIA removed it from consumer Ada GPUs). Memory is split, not pooled.

---

### 4. Single NVIDIA RTX 5090

**Verdict: Avoid at current market prices. Supply-constrained, overpriced, and still cannot fit 70B Q8 in VRAM alone.**

The RTX 5090 launched in January 2025 with MSRP of $1,999 but has never been available at that price in practice. As of May 2026, market prices range from $3,600–$5,500 depending on AIB model. Stock disappears within 30 minutes of restocking.

| Spec | Value |
|---|---|
| Total cost | $3,600–$5,500 (market rate, May 2026) + platform ~$600 = **$4,200–$6,100** |
| VRAM | 32GB GDDR7 |
| Memory bandwidth | 1,792 GB/s |
| Tokens/sec, 70B Q4 (fits: ~40GB needed vs 32GB VRAM — still must offload) | ~15–20 tok/s with partial CPU offload; ~35–45 tok/s if model fit entirely |
| Max model size (full in VRAM, Q4) | ~24B |
| 70B Q4 | Requires ~8GB CPU offload — moderate penalty |
| Idle power draw | ~15–20W GPU; ~60W system |
| Peak power draw | ~600W system (575W TDP GPU) |
| Annual electricity @ $0.15/kWh, 24/7 (75% load) | ~$590/yr |
| 3-year electricity cost | ~$1,770 |
| Thermal / noise | Single GPU, manageable. Loud under load (575W). |
| Ecosystem | CUDA. Full support for all frameworks. |

**Key weaknesses:**
- 32GB VRAM still does not fit a 70B Q4 model without offloading (~40GB needed). The headline bandwidth improvement is partially negated.
- Market price of $3,600–$5,500 for the GPU alone makes this extremely poor value vs. Mac Studio M4 Max at $3,699 complete system.
- Supply is deeply unreliable; you may wait months.
- If you want 70B without offload, you need 48GB+ VRAM — this GPU does not provide that.

**Add-ons needed:** Full ATX platform. Not self-contained.

---

### 5. NVIDIA RTX A6000 48GB (Used / Refurbished)

**Verdict: Interesting value play — professional-class GPU with full 48GB GDDR6, quiet passive cooling, but older Ampere architecture and limited market availability.**

The RTX A6000 is Ampere generation (2021), not Ada. It has 48GB GDDR6 at 768 GB/s bandwidth. The newer RTX 6000 Ada (also 48GB) has higher bandwidth (~960 GB/s) and is substantially more expensive ($6,500–$7,000 used). The Ampere A6000 can be found used for $2,500–$3,500.

| Spec | Value |
|---|---|
| Total cost (used A6000 + platform) | ~$3,000–$4,000 GPU + ~$700 platform = **$3,700–$4,700** |
| VRAM | 48GB GDDR6 |
| Memory bandwidth | 768 GB/s (Ampere A6000) |
| Tokens/sec, 70B Q4 | ~18–22 tok/s (all layers in VRAM) |
| Max model size (Q4) | ~40B fits fully; 70B Q4 fits with ~8GB remaining for KV |
| Max model size (Q8) | ~48GB = Qwen3 72B Q8 at 76GB does not fit |
| Idle power draw | ~20W GPU; ~80W system |
| Peak power draw | ~350–400W GPU; ~450W system |
| Annual electricity @ $0.15/kWh, 24/7 (60% load avg) | ~$385/yr |
| 3-year electricity cost | ~$1,155 |
| Thermal / noise | Professional workstation card with passive blower. Very quiet in a case with airflow. Designed for always-on operation. |
| Ecosystem | CUDA. Full support. |

**Key weaknesses:**
- Ampere (GA102) is two generations old. Ada (AD102) and Blackwell are faster per VRAM GB.
- 768 GB/s bandwidth is meaningfully lower than RTX 4090 (1,008 GB/s) or RTX 5090 (1,792 GB/s), resulting in lower token throughput.
- 70B Q4 fits but leaves ~8GB for KV cache — same tight headroom as dual 4090.
- Used market carries condition risk. Verify provenance.
- The RTX 6000 Ada (960 GB/s, same 48GB) is a much better card but costs $6,500–$7,000 used, breaking the budget.

**Add-ons needed:** Full workstation platform (Threadripper or Xeon W recommended for ECC memory support). ATX PSU 750W is sufficient.

---

### 6. Dual AMD RX 7900 XTX

**Verdict: Cheapest way to get 48GB GDDR6 on x86, but ROCm ecosystem immaturity is a real tax on developer time.**

The RX 7900 XTX has 24GB GDDR6 per card. Two cards provide 48GB total but without memory pooling (PCIe tensor parallelism only — ROCm lacks NVLink equivalent). RDNA 3 architecture, released late 2022.

| Spec | Value |
|---|---|
| Total cost | 2x RX 7900 XTX (~$600–$700 each used) + platform (~$700) = **$1,900–$2,800** |
| VRAM | 48GB total (24GB + 24GB, no pooling) |
| Memory bandwidth | 960 GB/s per card |
| Tokens/sec, 70B Q4 | ~12–16 tok/s (ROCm backend; llama.cpp HIP) |
| Ecosystem quality | ROCm 7.2 (March 2026) is now the first release with full Ollama/llama.cpp/vLLM parity. Still ~15% slower than CUDA on equivalent hardware. |
| Idle power draw | ~90W system (both GPUs at low idle) |
| Peak power draw | ~600–650W system |
| Annual electricity @ $0.15/kWh, 24/7 (60% load) | ~$510/yr |
| 3-year electricity cost | ~$1,530 |
| Thermal / noise | Consumer gaming cards. Hot and noisy under inference load. Not ideal for a home office. |

**Key weaknesses:**
- ROCm 7.2 (March 2026) is the first release with true parity with CUDA for llama.cpp and Ollama, but RDNA 3 still lags on ROCm-compiled kernels. For RDNA 4 (RX 9070 XT), the situation is slightly better with ROCm 7.2 but vLLM still has no native gfx1201 kernels and falls back to FP32 — a devastating performance cliff.
- Active llama.cpp issues (May 2026) document ROCm performance regressions on RDNA3 vs Vulkan. Vulkan backend on AMD can actually outperform ROCm in some workloads.
- No fine-tuning support: Axolotl, Unsloth, and most PEFT libraries require CUDA. You cannot fine-tune models on this hardware.
- Consumer card noise under 300W+ dual-GPU load.
- Support overhead: debugging ROCm issues is significantly more time-consuming than CUDA.

**Add-ons needed:** Full ATX platform. 1000W PSU minimum.

---

### 7. AMD RX 9070 XT (Single)

**Verdict: Wrong tier for the stated requirement. Cannot run 70B models without severe offloading. Fine for 13B–32B use cases.**

The RX 9070 XT is RDNA 4, released early 2026, with 16GB GDDR6 and ROCm 7.2 support. Benchmarks from May 2026 show 48 tok/s on 9B models via ROCm and 62 tok/s via Vulkan (Vulkan currently faster due to ROCm RDNA4 kernel gaps). Price: $650–$900.

A 70B Q4 model requires ~40GB VRAM. With only 16GB available, approximately 60% of the model must be CPU-offloaded, degrading performance to 3–6 tok/s. This is not a viable inference tier for 70B models.

**Not recommended for this use case.** Included for completeness only.

---

### 8. Refurbished Workstation + A100 80GB PCIe (Exceeds Budget)

**Verdict: Best single-card 70B inference story, but $6,000–$8,000 total cost exceeds the hard cap. Included as reference.**

A single A100 80GB PCIe provides 80GB HBM2e at ~2 TB/s bandwidth. A 70B Q4 model (~40GB) fits comfortably with room for long KV caches. A 70B Q8 model (~75GB) fits with minimal headroom. Performance: ~30–40 tok/s on 70B Q4.

Used A100 PCIe 80GB cards: $6,500–$9,000 (May 2026, varies by vendor). Plus a compatible PCIe workstation platform: $1,500–$2,500 (used Dell Precision 7960, HP Z8, Supermicro). Total: $8,000–$11,500. Well outside budget.

**If budget were $10k+**, this would be the strongest single-GPU option for always-on inference. The A100's HBM2e bandwidth gives it an edge over consumer GDDR6X cards at 80GB fill capacity, and the passive cooled data center card is appropriate for always-on operation.

---

## Rankings by Category

### Performance Per Dollar (tok/s per $1,000 spent)

1. **Dual RX 7900 XTX** — ~5–6 tok/s per $1k (cheap hardware, but real ROCm overhead)
2. **Mac Studio M4 Max 128GB** — ~4.3 tok/s per $1k (all-in $3,699 gets you 15–18 tok/s)
3. **RTX A6000 48GB (used)** — ~4.5–5 tok/s per $1k
4. **Dual RTX 4090** — ~3.5–4 tok/s per $1k (expensive build)
5. **RTX 5090 (single)** — ~2–3 tok/s per $1k (overpriced per unit, cannot fully fit 70B)

### Max Model Capacity

1. Mac Studio M3 Ultra 192GB — ~160B Q4, ~90B Q8 (over budget)
2. Mac Studio M4 Max 128GB — ~110B Q4, ~60B Q8
3. Dual RTX 4090 / Dual 7900 XTX / RTX A6000 48GB — ~40B Q4 fully cached; 70B Q4 with tight KV headroom
4. RTX 5090 — ~24B Q4 fully cached; 70B Q4 with CPU offload
5. A100 80GB (over budget) — 70B Q8 comfortably

### Power Efficiency (tok/s per watt at inference)

1. **Mac Studio M4 Max** — ~0.20–0.22 tok/s/W at 70B (best in class by far)
2. **Mac Studio M3 Ultra** — ~0.15 tok/s/W
3. **RTX A6000** — ~0.05 tok/s/W
4. **Dual RTX 4090** — ~0.025 tok/s/W
5. **Dual RX 7900 XTX** — ~0.025 tok/s/W

### 3-Year Total Cost of Ownership (Hardware + Electricity)

Assuming mixed 24/7 use (~40% inference load, ~60% idle):

| Build | Hardware | 3yr Elec. | 3yr TCO |
|---|---|---|---|
| Mac Studio M4 Max 128GB | $3,699 | ~$150 | **~$3,850** |
| Mac Studio M3 Ultra 192GB | $6,999 | ~$300 | ~$7,300 |
| RTX A6000 48GB (used) build | $4,200 | ~$780 | ~$4,980 |
| Dual RX 7900 XTX build | $2,800 | ~$950 | ~$3,750 |
| Dual RTX 4090 build | $5,700 | ~$1,900 | **~$7,600** |
| RTX 5090 build | $5,200 | ~$1,200 | ~$6,400 |

The dual RTX 4090 build has the worst 3-year TCO in the budget range. The Mac Studio M4 Max is essentially free to run by comparison.

### Ecosystem / Software Support

1. **Any CUDA build (RTX 4090, 5090, A6000)** — Gold standard. Full llama.cpp, Ollama, vLLM, exllamav2, TensorRT-LLM, Axolotl, Unsloth fine-tuning. No edge cases.
2. **Apple Silicon (M4 Max, M3 Ultra)** — Excellent for inference. llama.cpp Metal, Ollama Metal, MLX-LM, LM Studio. Cannot run vLLM. Cannot fine-tune with most frameworks. Growing rapidly but has gaps.
3. **AMD ROCm (7900 XTX, 9070 XT)** — Functional as of ROCm 7.2 (March 2026) for inference. ~15% slower than CUDA. vLLM has RDNA3/4 gaps. No fine-tuning support via consumer tools. Requires more debugging patience.

---

## Final Recommendation

**Primary recommendation: Mac Studio M4 Max 128GB at $3,699.**

- Fits the $3,500 target within $200
- Runs 70B Q4 at 15–18 tok/s — adequate for all single-user interactive use cases
- 3-year TCO of ~$3,850 is the lowest of any capable option
- Silent, compact, zero-maintenance for an always-on server role
- Can handle models up to ~110B at Q4 — Llama 4 Scout, Qwen3 72B, Llama 3.3 70B all run comfortably
- The 546 GB/s bandwidth is the only real constraint vs. M3 Ultra

**If the 70B speed ceiling (15–18 tok/s) is not acceptable** and budget allows bending to $5,000–$5,500: a used RTX A6000 48GB build gives similar VRAM (48GB) with a full CUDA ecosystem, slightly higher throughput, but dramatically higher electricity costs and noise. This is the right call if you want vLLM or plan to fine-tune.

**Do not buy:** a dual RTX 4090 build as an always-on server. The power cost is punishing and it does not fundamentally solve the 70B Q8 problem (48GB is still tight). The dual RX 7900 XTX is only worth considering if you are a Linux/ROCm power user who enjoys debugging ecosystem gaps.

---

## Sources

- [What to Buy for Local LLMs (April 2026) — Julien Simon](https://julsimon.medium.com/what-to-buy-for-local-llms-april-2026-a4946a381a6a)
- [Mac Studio M4 Max / M3 Ultra vs NVIDIA Blackwell — nixsense/xenix.blog](https://xenix.blog/2025/05/05/mac-studio-m4-max-m3-ultra-vs-nvidia-blackwell-which-desktop-reigns-for-local-genai/)
- [M4 Max and M3 Ultra for Local LLMs — InsiderLLM](https://insiderllm.com/guides/m4-max-ultra-local-llms-apple-silicon/)
- [Multi-GPU LLM Setup 2026 — Compute Market](https://www.compute-market.com/blog/multi-gpu-local-llm-setup-guide-2026)
- [Best GPUs for Local AI 2026 — Local AI Master](https://localaimaster.com/blog/best-gpus-for-ai-2025)
- [RTX 5090 Price May 2026 — GPU Poet](https://gpupoet.com/gpu/learn/price/may-2026/nvidia-geforce-rtx-5090)
- [RTX 4090 Price May 2026 — Best Value GPU](https://bestvaluegpu.com/history/new-and-used-rtx-4090-price-history-and-specs/)
- [M5 Mac Studio 2026 Rumors — Macworld](https://www.macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html)
- [Mac Studio Power Consumption — Apple Support](https://support.apple.com/en-us/102027)
- [Mac Studio M3 Ultra Cluster Idle Power — Tweaktown](https://www.tweaktown.com/news/103965/apple-mac-studio-cluster-4-m3-ultra-systems-use-half-the-power-of-network-switch-at-idle/index.html)
- [RX 9070 XT Vulkan vs ROCm Benchmarks — digtvbg.com](https://digtvbg.com/blog/llama-server-vulkan-rdna4-vllm-rocm-benchmark/)
- [ROCm Consumer GPU Guide 2026 — kunalganglani.com](https://www.kunalganglani.com/blog/rocm-consumer-gpu-cuda-alternative-2026)
- [llama.cpp ROCm Performance Discussion](https://github.com/ggml-org/llama.cpp/discussions/15021)
- [NVIDIA A100 80GB Price Guide 2025–2026 — directmacro](https://directmacro.com/blog/post/nvidia-a100-in-2025)
- [RTX 4090 Idle Power — igorslab.de](https://www.igorslab.de/en/nvidia-geforce-rtx-4090-founders-edition-24gb-review-drink-less-work-more/10/)
- [Local LLM Hardware Pricing Guide 2025 — Introl](https://introl.com/blog/local-llm-hardware-pricing-guide-2025)
