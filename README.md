# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-24 23:11:50 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `33.03 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `3.9 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `12.67 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `66.27 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `49.27 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `26.36`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,201.09 | 🔴 `-0.50%` |
| **Nasdaq Composite** (`^IXIC`) | $23,733.54 | 🔴 `-1.48%` |
| **Dow Jones** (`^DJI`) | $50,018.70 | 🟢 `+0.85%` |
| **Russell 2000** (`^RUT`) | $2,684.94 | 🟢 `+0.57%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $26.36 | 🔴 `-0.98%` |
| **US 10-Year Yield** (`^TNX`) | $4.90 | 🔴 `-0.28%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Healthcare** | `XLV` | 🟢 `+2.95%` | `+3.03%` |
| **Consumer Staples** | `XLP` | 🟢 `+1.66%` | `+4.46%` |
| **Real Estate** | `XLRE` | 🟢 `+1.31%` | `+1.54%` |
| **Energy** | `XLE` | 🟢 `+0.97%` | `-13.20%` |
| **Financials** | `XLF` | 🟢 `+0.83%` | `+0.16%` |
| **Consumer Discretionary** | `XLY` | 🟢 `+0.68%` | `+3.03%` |
| **Materials** | `XLB` | 🟢 `+0.54%` | `-2.36%` |
| **Utilities** | `XLU` | 🟢 `+0.18%` | `+2.00%` |
| **Industrials** | `XLI` | 🔴 `-0.53%` | `-3.20%` |
| **Technology** | `XLK` | 🔴 `-3.26%` | `-15.69%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **LLY** | $1,407.59 | 🟢 `+3.15%` | `48.69` | Bullish (Above 20-DMA) | **65 / 100** |
| **AAPL** | $354.07 | 🟢 `+1.43%` | `54.56` | Bullish (Above 20-DMA) | **59 / 100** |
| **BRK-B** | $577.21 | 🟢 `+0.85%` | `48.44` | Bullish (Above 20-DMA) | **53 / 100** |
| **TSLA** | $384.68 | 🔴 `-0.20%` | `49.87` | Bullish (Above 20-DMA) | **48 / 100** |
| **MSFT** | $496.13 | 🟢 `+0.74%` | `25.68` | Bearish (Below 20-DMA) | **41 / 100** |
| **GOOGL** | $279.05 | 🔴 `-1.08%` | `43.96` | Bearish (Below 20-DMA) | **41 / 100** |
| **AMZN** | $252.29 | 🔴 `-1.21%` | `41.02` | Bearish (Below 20-DMA) | **39 / 100** |
| **META** | $589.82 | 🔴 `-1.30%` | `40.97` | Bearish (Below 20-DMA) | **38 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
