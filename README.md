# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-20 21:25:47 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `67.77 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `38.67 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `99.59 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `85.09 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `47.74 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `37.25`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $6,910.39 | 🔴 `-3.70%` |
| **Nasdaq Composite** (`^IXIC`) | $22,617.73 | 🔴 `-5.28%` |
| **Dow Jones** (`^DJI`) | $48,147.33 | 🔴 `-1.93%` |
| **Russell 2000** (`^RUT`) | $2,581.79 | 🔴 `-2.76%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $37.25 | 🟢 `+30.98%` |
| **US 10-Year Yield** (`^TNX`) | $4.91 | 🔴 `-2.77%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Consumer Staples** | `XLP` | 🟢 `+0.72%` | `+3.90%` |
| **Healthcare** | `XLV` | 🔴 `-0.06%` | `-0.88%` |
| **Energy** | `XLE` | 🔴 `-0.49%` | `-11.11%` |
| **Utilities** | `XLU` | 🔴 `-0.67%` | `+1.71%` |
| **Real Estate** | `XLRE` | 🔴 `-0.93%` | `+1.00%` |
| **Financials** | `XLF` | 🔴 `-1.72%` | `-2.52%` |
| **Materials** | `XLB` | 🔴 `-2.14%` | `-5.77%` |
| **Consumer Discretionary** | `XLY` | 🔴 `-2.87%` | `-2.58%` |
| **Industrials** | `XLI` | 🔴 `-3.06%` | `-7.06%` |
| **Technology** | `XLK` | 🔴 `-7.10%` | `-20.82%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BRK-B** | $570.00 | 🔴 `-0.36%` | `59.12` | Bullish (Above 20-DMA) | **52 / 100** |
| **AAPL** | $342.56 | 🔴 `-1.90%` | `53.44` | Bearish (Below 20-DMA) | **42 / 100** |
| **LLY** | $1,347.11 | 🔴 `-0.30%` | `38.96` | Bearish (Below 20-DMA) | **42 / 100** |
| **MSFT** | $484.52 | 🔴 `-2.77%` | `43.13` | Bearish (Below 20-DMA) | **32 / 100** |
| **GOOGL** | $265.29 | 🔴 `-2.70%` | `40.47` | Bearish (Below 20-DMA) | **31 / 100** |
| **AMZN** | $246.82 | 🔴 `-4.10%` | `50.7` | Bearish (Below 20-DMA) | **29 / 100** |
| **JPM** | $310.68 | 🔴 `-2.98%` | `31.93` | Bearish (Below 20-DMA) | **26 / 100** |
| **META** | $560.84 | 🔴 `-5.93%` | `38.6` | Bearish (Below 20-DMA) | **14 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
