# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-24 05:27:15 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `18.07 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `3.69 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `12.62 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `31.34 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `24.63 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `26.62`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,237.17 | 🟢 `+4.73%` |
| **Nasdaq Composite** (`^IXIC`) | $24,089.56 | 🟢 `+6.51%` |
| **Dow Jones** (`^DJI`) | $49,595.31 | 🟢 `+3.01%` |
| **Russell 2000** (`^RUT`) | $2,669.66 | 🟢 `+3.40%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $26.62 | 🔴 `-25.83%` |
| **US 10-Year Yield** (`^TNX`) | $4.92 | 🟢 `+0.12%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Technology** | `XLK` | 🟢 `+8.97%` | `-12.85%` |
| **Consumer Discretionary** | `XLY` | 🟢 `+3.97%` | `+2.34%` |
| **Industrials** | `XLI` | 🟢 `+3.90%` | `-2.69%` |
| **Materials** | `XLB` | 🟢 `+3.23%` | `-2.88%` |
| **Financials** | `XLF` | 🟢 `+1.98%` | `-0.66%` |
| **Utilities** | `XLU` | 🟢 `+1.48%` | `+1.81%` |
| **Healthcare** | `XLV` | 🟢 `+1.23%` | `+0.08%` |
| **Real Estate** | `XLRE` | 🟢 `+1.04%` | `+0.23%` |
| **Consumer Staples** | `XLP` | 🔴 `-0.09%` | `+2.75%` |
| **Energy** | `XLE` | 🔴 `-1.06%` | `-14.03%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **NVDA** | $165.05 | 🟢 `+31.48%` | `35.18` | Bearish (Below 20-DMA) | **99 / 100** |
| **TSLA** | $385.46 | 🟢 `+11.46%` | `46.86` | Bullish (Above 20-DMA) | **99 / 100** |
| **GOOGL** | $282.10 | 🟢 `+6.34%` | `51.18` | Bearish (Below 20-DMA) | **82 / 100** |
| **AMD** | $453.46 | 🟢 `+6.85%` | `47.04` | Bearish (Below 20-DMA) | **82 / 100** |
| **META** | $597.60 | 🟢 `+6.55%` | `44.76` | Bearish (Below 20-DMA) | **80 / 100** |
| **AMZN** | $255.39 | 🟢 `+3.47%` | `52.65` | Bearish (Below 20-DMA) | **68 / 100** |
| **AAPL** | $349.08 | 🟢 `+1.90%` | `63.3` | Bullish (Above 20-DMA) | **66 / 100** |
| **AVGO** | $313.55 | 🟢 `+3.00%` | `45.85` | Bearish (Below 20-DMA) | **62 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
