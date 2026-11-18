# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-18 03:04:07 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `78.75 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `29.12 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `88.83 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `144.21 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `52.84 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `25.46`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,340.53 | 🔴 `-1.03%` |
| **Nasdaq Composite** (`^IXIC`) | $24,328.38 | 🔴 `-0.74%` |
| **Dow Jones** (`^DJI`) | $0.00 | 🟢 `+0.00%` |
| **Russell 2000** (`^RUT`) | $2,701.87 | 🔴 `-1.50%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $25.46 | 🟢 `+11.13%` |
| **US 10-Year Yield** (`^TNX`) | $5.10 | 🔴 `-0.35%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Energy** | `XLE` | 🔴 `-0.52%` | `-6.55%` |
| **Industrials** | `XLI` | 🔴 `-0.55%` | `-1.16%` |
| **Consumer Discretionary** | `XLY` | 🔴 `-0.89%` | `+2.31%` |
| **Technology** | `XLK` | 🔴 `-0.91%` | `-12.21%` |
| **Materials** | `XLB` | 🔴 `-1.22%` | `-0.22%` |
| **Consumer Staples** | `XLP` | 🔴 `-1.23%` | `+4.87%` |
| **Healthcare** | `XLV` | 🔴 `-1.41%` | `+5.46%` |
| **Real Estate** | `XLRE` | 🔴 `-1.49%` | `+4.61%` |
| **Utilities** | `XLU` | 🔴 `-1.59%` | `+4.98%` |
| **Financials** | `XLF` | 🔴 `-1.91%` | `+3.65%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AVGO** | $341.60 | 🟢 `+2.46%` | `47.34` | Bullish (Above 20-DMA) | **60 / 100** |
| **BRK-B** | $586.76 | 🔴 `-1.03%` | `80.87` | Bullish (Above 20-DMA) | **60 / 100** |
| **LLY** | $1,415.55 | 🔴 `-1.13%` | `68.46` | Bullish (Above 20-DMA) | **53 / 100** |
| **AAPL** | $351.91 | 🔴 `-0.25%` | `55.9` | Bullish (Above 20-DMA) | **51 / 100** |
| **AMZN** | $257.89 | 🟢 `+0.05%` | `52.22` | Bullish (Above 20-DMA) | **51 / 100** |
| **TSLA** | $380.11 | 🟢 `+0.10%` | `41.41` | Bearish (Below 20-DMA) | **46 / 100** |
| **AMD** | $503.41 | 🔴 `-0.17%` | `42.2` | Bearish (Below 20-DMA) | **45 / 100** |
| **META** | $618.87 | 🔴 `-1.20%` | `51.84` | Bearish (Below 20-DMA) | **44 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
