# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-18 21:30:50 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `94.08 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `8.09 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `29.11 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `167.08 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `172.03 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `24.56`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,323.63 | 🔴 `-0.23%` |
| **Nasdaq Composite** (`^IXIC`) | $24,429.88 | 🟢 `+0.42%` |
| **Dow Jones** (`^DJI`) | $50,198.17 | 🔴 `-1.11%` |
| **Russell 2000** (`^RUT`) | $2,714.31 | 🟢 `+0.46%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $24.56 | 🔴 `-3.53%` |
| **US 10-Year Yield** (`^TNX`) | $5.07 | 🔴 `-0.73%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Consumer Discretionary** | `XLY` | 🟢 `+1.79%` | `+4.14%` |
| **Technology** | `XLK` | 🟢 `+0.34%` | `-11.91%` |
| **Utilities** | `XLU` | 🟢 `+0.30%` | `+5.29%` |
| **Real Estate** | `XLRE` | 🟢 `+0.07%` | `+4.68%` |
| **Industrials** | `XLI` | 🔴 `-0.05%` | `-1.21%` |
| **Consumer Staples** | `XLP` | 🔴 `-0.31%` | `+4.55%` |
| **Materials** | `XLB` | 🔴 `-0.75%` | `-0.96%` |
| **Financials** | `XLF` | 🔴 `-1.14%` | `+2.47%` |
| **Healthcare** | `XLV` | 🔴 `-2.20%` | `+3.14%` |
| **Energy** | `XLE` | 🔴 `-3.27%` | `-9.60%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AMZN** | $267.74 | 🟢 `+3.82%` | `66.39` | Bullish (Above 20-DMA) | **77 / 100** |
| **AMD** | $530.14 | 🟢 `+5.31%` | `46.34` | Bullish (Above 20-DMA) | **74 / 100** |
| **AVGO** | $354.05 | 🟢 `+3.64%` | `52.29` | Bullish (Above 20-DMA) | **69 / 100** |
| **GOOGL** | $282.44 | 🟢 `+0.80%` | `48.84` | Bearish (Below 20-DMA) | **53 / 100** |
| **AAPL** | $352.45 | 🟢 `+0.15%` | `52.88` | Bullish (Above 20-DMA) | **52 / 100** |
| **TSLA** | $383.72 | 🟢 `+0.95%` | `43.16` | Bearish (Below 20-DMA) | **51 / 100** |
| **BRK-B** | $574.62 | 🔴 `-2.07%` | `69.05` | Bullish (Above 20-DMA) | **49 / 100** |
| **MSFT** | $508.29 | 🟢 `+0.40%` | `43.08` | Bearish (Below 20-DMA) | **48 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
