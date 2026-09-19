#!/usr/bin/env python3
"""README Generator for System Pulse.

Combines infrastructure heartbeat metrics and quantitative market pulse into
a dynamic, real-time dashboard in README.md.
"""

from datetime import datetime, timezone
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
README_PATH = ROOT_DIR / "README.md"
INFRA_LATEST = ROOT_DIR / "data" / "infra" / "latest.json"
MARKET_LATEST = ROOT_DIR / "data" / "market" / "latest.json"


def generate_readme() -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    infra = {}
    if INFRA_LATEST.exists():
        try:
            infra = json.loads(INFRA_LATEST.read_text())
        except Exception:
            pass

    market = {}
    if MARKET_LATEST.exists():
        try:
            market = json.loads(MARKET_LATEST.read_text())
        except Exception:
            pass

    # Status badges
    infra_status = infra.get("overall_status", "operational").upper()
    uptime = infra.get("uptime_percent", 100)
    avg_lat = infra.get("average_latency_ms", 0)
    regime = market.get("market_regime", "Active")

    badge_color = "brightgreen" if infra_status == "HEALTHY" else "yellow"
    
    lines = [
        "# ⚡ System Pulse",
        "",
        f"[![Infrastructure Uptime](https://img.shields.io/badge/Infrastructure-{uptime}%25%20Uptime-{badge_color}?style=for-the-badge&logo=oracle)]()",
        f"[![Market Regime](https://img.shields.io/badge/Market%20Regime-{regime.split()[0]}-blue?style=for-the-badge&logo=tradingview)]()",
        f"[![Automated Sync](https://img.shields.io/badge/Telemetry-Automated%20GitHub%20Actions-purple?style=for-the-badge&logo=githubactions)]()",
        "",
        "> **System Pulse** is an automated dual-engine telemetry dashboard. It monitors 24/7 cloud infrastructure health across Oracle Cloud / APIs and generates daily quantitative market sector momentum & factor scores at market close.",
        "",
        f"*Last Telemetry Refresh: `{now_utc}`*",
        "",
        "---",
        "",
        "## 🛰️ 1. Cloud Infrastructure & Service Health",
        "",
        f"**Overall Status:** `{'🟢 Operational' if uptime == 100 else '🟡 Degraded'}` | **Uptime:** `{uptime}%` | **Avg Latency:** `{avg_lat} ms`",
        "",
        "| Monitored Service | Target / Endpoint | Status | Response Time |",
        "| :--- | :--- | :---: | :---: |",
    ]

    for svc in infra.get("services", []):
        icon = "🟢 UP" if svc.get("status") == "up" else ("🟡 DEGRADED" if svc.get("status") == "degraded" else "🔴 DOWN")
        lat = f"`{svc.get('latency_ms', 0)} ms`"
        note = f" *(code: {svc.get('code')})*" if svc.get("code") else ""
        lines.append(f"| **{svc.get('name')}** | `{svc.get('url')}` | {icon} | {lat}{note} |")

    lines.extend([
        "",
        "---",
        "",
        "## 📈 2. Daily Market Pulse & Sector Momentum",
        "",
        f"**Macro Regime:** `{regime}` | **VIX Volatility:** `{market.get('vix_level', 'N/A')}`",
        "",
        "### 📊 Major Indices",
        "| Index | Level | 1-Day Change |",
        "| :--- | :---: | :---: |",
    ])

    for idx in market.get("indices", []):
        chg = idx.get("change_pct", 0)
        chg_icon = "🟢" if chg >= 0 else "🔴"
        lines.append(f"| **{idx.get('name')}** (`{idx.get('ticker')}`) | ${idx.get('price', 0):,.2f} | {chg_icon} `{chg:+.2f}%` |")

    lines.extend([
        "",
        "### 🏢 Sector Rotation Heatmap",
        "| Sector | ETF Ticker | 1-Day Change | 1-Month Trend |",
        "| :--- | :---: | :---: | :---: |",
    ])

    for sec in market.get("sectors", []):
        d_chg = sec.get("day_change_pct", 0)
        m_chg = sec.get("month_change_pct", 0)
        d_icon = "🟢" if d_chg >= 0 else "🔴"
        lines.append(f"| **{sec.get('sector')}** | `{sec.get('ticker')}` | {d_icon} `{d_chg:+.2f}%` | `{m_chg:+.2f}%` |")

    lines.extend([
        "",
        "### 🎯 Top Momentum & Conviction Factor Rankings",
        "| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Conviction Score |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |",
    ])

    for stk in market.get("top_movers", [])[:8]:
        s_chg = stk.get("day_change_pct", 0)
        s_icon = "🟢" if s_chg >= 0 else "🔴"
        lines.append(f"| **{stk.get('ticker')}** | ${stk.get('price', 0):,.2f} | {s_icon} `{s_chg:+.2f}%` | `{stk.get('rsi14')}` | {stk.get('trend_20d')} | **{stk.get('momentum_score')} / 100** |")

    lines.extend([
        "",
        "---",
        "",
        "## ⚙️ Architecture & Automated Execution",
        "",
        "- **Cloud Uptime Monitoring:** Executes automated HTTP/TCP probes verifying backend API latency and uptime.",
        "- **Quantitative ML Engine:** Ingests market closing feeds, computing 14-period RSI, moving average trends, and multi-factor ranking signals.",
        "- **Scheduled CI/CD Pipeline:** Powered by GitHub Actions running twice daily on schedule (`13:30 UTC` pre-market & `21:30 UTC` market close).",
        "",
        "---",
        "",
        "### 👤 Author",
        "**Benjamin Bamisile** ([@benjaminbob21](https://github.com/benjaminbob21))  ",
        "Automated SRE & Quantitative Engineering Stack",
    ])

    readme_content = "\n".join(lines) + "\n"
    README_PATH.write_text(readme_content)
    print("README.md successfully updated.")
    return readme_content


if __name__ == "__main__":
    generate_readme()
