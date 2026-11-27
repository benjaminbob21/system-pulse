# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-27 22:14:12 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `75.3 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `61.41 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `15.28 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `198.18 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `26.33 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `23.81`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,297.49 | 🟢 `+1.60%` |
| **Nasdaq Composite** (`^IXIC`) | $24,129.50 | 🟢 `+2.31%` |
| **Dow Jones** (`^DJI`) | $50,774.94 | 🟢 `+1.18%` |
| **Russell 2000** (`^RUT`) | $2,750.30 | 🟢 `+1.71%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $23.81 | 🔴 `-11.16%` |
| **US 10-Year Yield** (`^TNX`) | $4.94 | 🟢 `+1.82%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Technology** | `XLK` | 🟢 `+2.80%` | `-16.15%` |
| **Consumer Discretionary** | `XLY` | 🟢 `+2.11%` | `+4.02%` |
| **Materials** | `XLB` | 🟢 `+1.84%` | `+0.56%` |
| **Industrials** | `XLI` | 🟢 `+1.60%` | `-1.74%` |
| **Energy** | `XLE` | 🟢 `+1.26%` | `-9.91%` |
| **Financials** | `XLF` | 🟢 `+1.15%` | `+1.84%` |
| **Real Estate** | `XLRE` | 🟢 `+0.64%` | `+4.77%` |
| **Consumer Staples** | `XLP` | 🟢 `+0.41%` | `+6.73%` |
| **Healthcare** | `XLV` | 🟢 `+0.28%` | `+2.49%` |
| **Utilities** | `XLU` | 🟢 `+0.28%` | `+2.92%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TSLA** | $400.00 | 🟢 `+5.22%` | `62.77` | Bullish (Above 20-DMA) | **82 / 100** |
| **AMD** | $424.54 | 🟢 `+4.56%` | `47.25` | Bearish (Below 20-DMA) | **71 / 100** |
| **AVGO** | $312.34 | 🟢 `+3.82%` | `54.54` | Bearish (Below 20-DMA) | **71 / 100** |
| **AMZN** | $254.12 | 🟢 `+3.96%` | `47.04` | Bearish (Below 20-DMA) | **68 / 100** |
| **META** | $628.96 | 🟢 `+3.13%` | `54.06` | Bullish (Above 20-DMA) | **67 / 100** |
| **AAPL** | $358.54 | 🟢 `+0.83%` | `66.35` | Bullish (Above 20-DMA) | **62 / 100** |
| **JPM** | $322.96 | 🟢 `+1.96%` | `40.65` | Bearish (Below 20-DMA) | **55 / 100** |
| **BRK-B** | $580.79 | 🟢 `+0.25%` | `58.87` | Bullish (Above 20-DMA) | **55 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
