# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-08 06:22:58 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `62.59 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `66.33 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `56.37 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `66.28 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `61.4 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `25.64`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,376.86 | 🟢 `+0.31%` |
| **Nasdaq Composite** (`^IXIC`) | $24,579.43 | 🟢 `+1.09%` |
| **Dow Jones** (`^DJI`) | $51,285.73 | 🔴 `-0.46%` |
| **Russell 2000** (`^RUT`) | $2,754.11 | 🟢 `+0.89%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $25.64 | 🔴 `-9.01%` |
| **US 10-Year Yield** (`^TNX`) | $4.86 | 🟢 `+0.45%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Technology** | `XLK` | 🟢 `+1.45%` | `-18.20%` |
| **Industrials** | `XLI` | 🟢 `+0.12%` | `-3.08%` |
| **Energy** | `XLE` | 🔴 `-0.02%` | `-2.75%` |
| **Consumer Discretionary** | `XLY` | 🔴 `-0.05%` | `+5.59%` |
| **Healthcare** | `XLV` | 🔴 `-0.06%` | `+9.47%` |
| **Utilities** | `XLU` | 🔴 `-0.39%` | `+4.81%` |
| **Financials** | `XLF` | 🔴 `-0.59%` | `+6.34%` |
| **Real Estate** | `XLRE` | 🔴 `-0.68%` | `+8.45%` |
| **Materials** | `XLB` | 🔴 `-0.73%` | `+6.06%` |
| **Consumer Staples** | `XLP` | 🔴 `-1.28%` | `+10.26%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **AMD** | $449.04 | 🟢 `+11.04%` | `38.85` | Bearish (Below 20-DMA) | **99 / 100** |
| **TSLA** | $358.22 | 🟢 `+4.23%` | `46.81` | Bearish (Below 20-DMA) | **69 / 100** |
| **BRK-B** | $570.89 | 🔴 `-0.25%` | `73.37` | Bullish (Above 20-DMA) | **60 / 100** |
| **LLY** | $1,354.00 | 🔴 `-0.79%` | `66.23` | Bullish (Above 20-DMA) | **54 / 100** |
| **NVDA** | $186.64 | 🟢 `+2.78%` | `29.63` | Bearish (Below 20-DMA) | **53 / 100** |
| **AAPL** | $342.37 | 🔴 `-0.52%` | `49.59` | Bearish (Below 20-DMA) | **47 / 100** |
| **AMZN** | $259.30 | 🔴 `-0.35%` | `47.69` | Bullish (Above 20-DMA) | **47 / 100** |
| **JPM** | $334.49 | 🔴 `-0.84%` | `50.74` | Bearish (Below 20-DMA) | **46 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
