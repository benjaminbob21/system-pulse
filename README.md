# ⚡ System Pulse

[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-100.0%25%20Uptime-brightgreen?style=for-the-badge&logo=oracle)]()
[![Market Regime](https://img.shields.io/badge/Market%20Regime-Risk-Off-blue?style=for-the-badge&logo=tradingview)]()
[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()

> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.

*Last Telemetry Refresh: `2026-11-27 03:43:39 UTC`*

---

## 🛰️ 1. Cloud Infrastructure & Service Health

**Overall Status:** `🟢 Operational` | **Uptime:** `100.0%` | **Avg Latency:** `90.2 ms`

| Monitored Service | Target / Endpoint | Status | Response Time |
| :--- | :--- | :---: | :---: |
| **Oracle Always-Free Production Cluster** | `tcp://cloud-node-01.internal:22` | 🟢 UP | `81.35 ms` *(code: 200)* |
| **GitHub Core API** | `https://api.github.com/zen` | 🟢 UP | `45.94 ms` *(code: 200)* |
| **SEC EDGAR API Gateway** | `https://data.sec.gov/submissions/...` | 🟢 UP | `207.34 ms` *(code: 200)* |
| **PyPI Package Registry** | `https://pypi.org/pypi/requests/json` | 🟢 UP | `26.16 ms` *(code: 200)* |

---

## 📈 2. Daily Market Pulse & Sector Momentum

**Macro Regime:** `Risk-Off (High Volatility / Defensive)` | **VIX Volatility:** `26.8`

### 📊 Major Indices
| Index | Level | 1-Day Change |
| :--- | :---: | :---: |
| **S&P 500** (`^GSPC`) | $7,182.78 | 🔴 `-0.25%` |
| **Nasdaq Composite** (`^IXIC`) | $23,585.80 | 🔴 `-0.62%` |
| **Dow Jones** (`^DJI`) | $50,182.95 | 🟢 `+0.33%` |
| **Russell 2000** (`^RUT`) | $2,704.06 | 🟢 `+0.71%` |
| **CBOE Volatility (VIX)** (`^VIX`) | $26.80 | 🔴 `-5.27%` |
| **US 10-Year Yield** (`^TNX`) | $4.85 | 🔴 `-1.14%` |

### 🏢 Sector Rotation Heatmap
| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |
| :--- | :---: | :---: | :---: |
| **Materials** | `XLB` | 🟢 `+2.07%` | `-0.33%` |
| **Real Estate** | `XLRE` | 🟢 `+0.92%` | `+2.48%` |
| **Industrials** | `XLI` | 🟢 `+0.83%` | `-2.40%` |
| **Energy** | `XLE` | 🟢 `+0.74%` | `-12.55%` |
| **Financials** | `XLF` | 🟢 `+0.71%` | `+0.87%` |
| **Utilities** | `XLU` | 🟢 `+0.48%` | `+2.49%` |
| **Consumer Staples** | `XLP` | 🟢 `+0.46%` | `+4.93%` |
| **Consumer Discretionary** | `XLY` | 🔴 `-0.20%` | `+2.83%` |
| **Healthcare** | `XLV` | 🔴 `-0.56%` | `+2.45%` |
| **Technology** | `XLK` | 🔴 `-0.83%` | `-16.39%` |

### 🎯 Top Momentum & Conviction Factor Rankings
| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **META** | $609.89 | 🟢 `+3.40%` | `51.11` | Bearish (Below 20-DMA) | **67 / 100** |
| **AAPL** | $355.58 | 🟢 `+0.43%` | `61.89` | Bullish (Above 20-DMA) | **58 / 100** |
| **BRK-B** | $579.32 | 🟢 `+0.37%` | `56.27` | Bullish (Above 20-DMA) | **54 / 100** |
| **AVGO** | $300.86 | 🔴 `-0.07%` | `52.38` | Bearish (Below 20-DMA) | **50 / 100** |
| **TSLA** | $380.14 | 🔴 `-1.18%` | `61.51` | Bearish (Below 20-DMA) | **49 / 100** |
| **LLY** | $1,392.22 | 🔴 `-1.09%` | `54.95` | Bearish (Below 20-DMA) | **47 / 100** |
| **AMD** | $406.03 | 🔴 `-1.75%` | `50.17` | Bearish (Below 20-DMA) | **41 / 100** |
| **JPM** | $316.74 | 🔴 `-0.11%` | `32.33` | Bearish (Below 20-DMA) | **40 / 100** |

---

## ⚙️ Architecture & Automated Execution

- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.
- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.
- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).

---

### 👤 Author
**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  
Automated SRE & Quantitative Engineering Stack
