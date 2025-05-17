import yfinance as yf
from datetime import datetime

tickers = {
    "S&P500": "^GSPC",
    "NASDAQ": "^IXIC",
    "USD/JPY": "JPY=X",
    "WTI原油": "CL=F",
    "金": "GC=F"
}

summary = f"【NY市場サマリー】{datetime.now().strftime('%Y/%m/%d')}\n\n"

for name, symbol in tickers.items():
    data = yf.Ticker(symbol).history(period="2d")
    if len(data) >= 2:
        prev = data['Close'].iloc[-2]
        last = data['Close'].iloc[-1]
        diff = last - prev
        pct = (diff / prev) * 100
        summary += f"{name}: {last:.2f}（{diff:+.2f}, {pct:+.2f}%）\n"

print(summary)

import requests  # すでにあれば重複不要

discord_webhook_url = "https://canary.discord.com/api/webhooks/1373190262922416169/GWl9uyxmMKV-pkVY6e-Nr6wl2UUPuBr6unuZDULqBHjU0y-Dm4hb1Rpbq8tYEMN3hDdM"

# Discordにメッセージ送信
requests.post(
    discord_webhook_url,
    json={"content": summary}
)
