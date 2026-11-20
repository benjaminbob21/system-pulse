# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-20 02:30:28 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `82.02 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `25.05 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `96.97 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `160.11 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `45.94 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `28.44`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,175.83 | 🔴 `-2.02%` |
| **Nasdaq Composite** (`^IXIC`) | $23,879.20 | 🔴 `-2.25%` |
| **Dow Jones** (`^DJI`) | $49,097.06 | 🔴 `-2.19%` |
| **Russell 2000** (`^RUT`) | $2,655.11 | 🔴 `-2.18%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $28.44 | 🟢 `+15.80%` |
| **US 10-Year Yield** (`^TNX`) | $0.00 | 🟢 `+0.00%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Real Estate** | `XLRE` | 🟢 `+0.07%` | `+2.93%` |
| **Energy** | `XLE` | 🔴 `-0.65%` | `-10.42%` |
| **Utilities** | `XLU` | 🔴 `-1.24%` | `+2.70%` |
| **Consumer Staples** | `XLP` | 🔴 `-1.45%` | `+2.40%` |
| **Financials** | `XLF` | 🔴 `-1.49%` | `-0.25%` |
| **Technology** | `XLK` | 🔴 `-1.90%` | `-13.35%` |
| **Industrials** | `XLI` | 🔴 `-2.00%` | `-3.26%` |
| **Healthcare** | `XLV` | 🔴 `-2.05%` | `-1.31%` |
| **Materials** | `XLB` | 🔴 `-2.06%` | `-3.53%` |
| **Consumer Discretionary** | `XLY` | 🔴 `-2.79%` | `+0.33%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BRK-B** | $572.04 | 🔴 `-0.45%` | `66.84` | Bullish (Above 20-DMA) | **56 / 100** |
| **AAPL** | $349.21 | 🔴 `-0.92%` | `53.72` | Bullish (Above 20-DMA) | **47 / 100** |
| **META** | $616.38 | 🔴 `-0.40%` | `47.51` | Bearish (Below 20-DMA) | **46 / 100** |
| **AVGO** | $346.65 | 🔴 `-2.09%` | `55.52` | Bullish (Above 20-DMA) | **42 / 100** |
| **JPM** | $320.22 | 🔴 `-1.20%` | `39.04` | Bearish (Below 20-DMA) | **38 / 100** |
| **MSFT** | $498.30 | 🔴 `-1.78%` | `42.87` | Bearish (Below 20-DMA) | **37 / 100** |
| **AMZN** | $257.37 | 🔴 `-3.87%` | `60.64` | Bearish (Below 20-DMA) | **35 / 100** |
| **TSLA** | $374.41 | 🔴 `-2.43%` | `41.47` | Bearish (Below 20-DMA) | **33 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
