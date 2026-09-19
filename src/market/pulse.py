#!/usr/bin/env python3
"""Daily Market Pulse & Quantitative Sector Momentum.

Pulls index performance, sector rankings, and high-conviction factor momentum.
"""

from datetime import datetime, timezone
import json
from pathlib import Path
import yfinance as yf
import pandas as pd
import numpy as np

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / "data" / "market"

INDICES = {
    "^GSPC": "S&P 500",
    "^IXIC": "Nasdaq Composite",
    "^DJI": "Dow Jones",
    "^RUT": "Russell 2000",
    "^VIX": "CBOE Volatility (VIX)",
    "^TNX": "US 10-Year Yield",
}

SECTORS = {
    "XLK": "Technology",
    "XLF": "Financials",
    "XLV": "Healthcare",
    "XLE": "Energy",
    "XLI": "Industrials",
    "XLY": "Consumer Discretionary",
    "XLP": "Consumer Staples",
    "XLU": "Utilities",
    "XLB": "Materials",
    "XLRE": "Real Estate",
}

WATCHLIST = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "AMD", "AVGO", "JPM", "LLY", "BRK-B"]


def calculate_rsi(series: pd.Series, period: int = 14) -> float:
    if len(series) < period + 1:
        return 50.0
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    
    last_gain = avg_gain.iloc[-1]
    last_loss = avg_loss.iloc[-1]
    
    if last_loss == 0 or np.isnan(last_loss):
        return 100.0 if last_gain > 0 else 50.0
    rs = last_gain / last_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return round(float(rsi), 2)


def collect_market_pulse() -> dict:
    now_utc = datetime.now(timezone.utc)
    
    # 1. Fetch Major Indices
    index_tickers = list(INDICES.keys())
    idx_data = yf.download(index_tickers, period="5d", interval="1d", progress=False)["Close"]
    
    index_results = []
    for ticker, name in INDICES.items():
        try:
            series = idx_data[ticker].dropna() if ticker in idx_data else pd.Series()
            if len(series) >= 2:
                current_price = float(series.iloc[-1])
                prev_price = float(series.iloc[-2])
                change_pct = round(((current_price - prev_price) / prev_price) * 100, 2)
            else:
                current_price = 0.0
                change_pct = 0.0
            
            index_results.append({
                "ticker": ticker,
                "name": name,
                "price": round(current_price, 2),
                "change_pct": change_pct,
            })
        except Exception:
            index_results.append({"ticker": ticker, "name": name, "price": 0.0, "change_pct": 0.0})

    # 2. Fetch Sector Performance
    sector_tickers = list(SECTORS.keys())
    sec_data = yf.download(sector_tickers, period="1mo", interval="1d", progress=False)["Close"]
    
    sector_results = []
    for ticker, name in SECTORS.items():
        try:
            series = sec_data[ticker].dropna() if ticker in sec_data else pd.Series()
            if len(series) >= 2:
                curr = float(series.iloc[-1])
                prev_day = float(series.iloc[-2])
                day_change = round(((curr - prev_day) / prev_day) * 100, 2)
                
                start_month = float(series.iloc[0])
                month_change = round(((curr - start_month) / start_month) * 100, 2)
            else:
                curr, day_change, month_change = 0.0, 0.0, 0.0
            
            sector_results.append({
                "ticker": ticker,
                "sector": name,
                "price": round(curr, 2),
                "day_change_pct": day_change,
                "month_change_pct": month_change,
            })
        except Exception:
            sector_results.append({"ticker": ticker, "sector": name, "price": 0.0, "day_change_pct": 0.0, "month_change_pct": 0.0})

    # Sort sectors by 1-day momentum
    sector_results.sort(key=lambda x: x["day_change_pct"], reverse=True)

    # 3. Compute Stock Watchlist Factors (RSI, 20DMA Trend, Volatility)
    stock_data = yf.download(WATCHLIST, period="3mo", interval="1d", progress=False)["Close"]
    stock_results = []
    
    for ticker in WATCHLIST:
        try:
            series = stock_data[ticker].dropna() if ticker in stock_data else pd.Series()
            if len(series) >= 20:
                curr = float(series.iloc[-1])
                prev = float(series.iloc[-2])
                day_change = round(((curr - prev) / prev) * 100, 2)
                
                ma20 = float(series.tail(20).mean())
                trend_20d = "Bullish (Above 20-DMA)" if curr > ma20 else "Bearish (Below 20-DMA)"
                rsi14 = calculate_rsi(series, period=14)
                
                # Simple quantitative momentum score (0-100)
                momentum_score = int(np.clip(50 + (day_change * 5) + ((rsi14 - 50) * 0.5), 10, 99))
                
                stock_results.append({
                    "ticker": ticker,
                    "price": round(curr, 2),
                    "day_change_pct": day_change,
                    "rsi14": rsi14,
                    "trend_20d": trend_20d,
                    "momentum_score": momentum_score,
                })
        except Exception:
            pass

    stock_results.sort(key=lambda x: x["momentum_score"], reverse=True)

    # Determine market sentiment regime
    vix_item = next((x for x in index_results if x["ticker"] == "^VIX"), None)
    vix_val = vix_item["price"] if vix_item else 16.0
    if vix_val < 15:
        regime = "Risk-On (Low Volatility)"
    elif vix_val < 22:
        regime = "Neutral / Stable"
    else:
        regime = "Risk-Off (High Volatility / Defensive)"

    pulse_data = {
        "timestamp": now_utc.isoformat(),
        "formatted_time": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "date": now_utc.strftime("%Y-%m-%d"),
        "market_regime": regime,
        "vix_level": vix_val,
        "indices": index_results,
        "sectors": sector_results,
        "top_movers": stock_results,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save latest JSON
    latest_file = DATA_DIR / "latest.json"
    latest_file.write_text(json.dumps(pulse_data, indent=2))

    # Save daily Markdown report
    md_report = generate_markdown_report(pulse_data)
    report_file = DATA_DIR / f"{pulse_data['date']}.md"
    report_file.write_text(md_report)

    print(f"[{pulse_data['formatted_time']}] Market Pulse Generated: Regime={regime} | Top Sector={sector_results[0]['sector']}")
    return pulse_data


def generate_markdown_report(data: dict) -> str:
    lines = [
        f"# Daily Market Pulse — {data['date']}",
        f"**Generated:** {data['formatted_time']}  ",
        f"**Market Regime:** `{data['market_regime']}` (VIX: `{data['vix_level']}`)\n",
        "## 📊 Major Indices",
        "| Index | Price | Daily Change |",
        "| :--- | :--- | :--- |",
    ]
    for idx in data["indices"]:
        chg_icon = "🟢" if idx["change_pct"] >= 0 else "🔴"
        lines.append(f"| **{idx['name']}** (`{idx['ticker']}`) | ${idx['price']:,.2f} | {chg_icon} `{idx['change_pct']:+.2f}%` |")

    lines.extend([
        "\n## 🏢 Sector Momentum Heatmap",
        "| Sector | ETF | 1-Day Change | 1-Month Trend |",
        "| :--- | :--- | :--- | :--- |",
    ])
    for sec in data["sectors"]:
        day_icon = "🟢" if sec["day_change_pct"] >= 0 else "🔴"
        lines.append(f"| **{sec['sector']}** | `{sec['ticker']}` | {day_icon} `{sec['day_change_pct']:+.2f}%` | `{sec['month_change_pct']:+.2f}%` |")

    lines.extend([
        "\n## 🚀 Factor Momentum & Conviction Rankings",
        "| Ticker | Price | 1-Day % | RSI (14) | 20-DMA Trend | Score |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ])
    for stk in data["top_movers"]:
        s_icon = "🟢" if stk["day_change_pct"] >= 0 else "🔴"
        lines.append(f"| **{stk['ticker']}** | ${stk['price']:,.2f} | {s_icon} `{stk['day_change_pct']:+.2f}%` | `{stk['rsi14']}` | {stk['trend_20d']} | **{stk['momentum_score']} / 100** |")

    return "\n".join(lines)


if __name__ == "__main__":
    collect_market_pulse()
