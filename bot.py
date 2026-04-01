import requests
import time
import os

# =========================
# ENV VARIABLES (SAFE)
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://www.hmtwatches.in/product_overview?id=eyJpdiI6IlhnZS9EemVhTXJnU09aL1VtSndnWUE9PSIsInZhbHVlIjoiSGdCM3l3a2RGQTNhZUxSTnhpUEtjZz09IiwibWFjIjoiZThiZWQyNGMzNjA4MThmZDRhYmYxNDFlYTE1ZTU2YTAxY2NlNWNlNGJhNjZmNzQ0OWZkMjA4OTcyYzQ3ZmY3NyIsInRhZyI6IiJ9"

# =========================
# TELEGRAM FUNCTION
# =========================
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

print("Starting container...")

# Startup message
send_telegram("✅ Bot is running (secure version)")

in_stock_last_time = False

# =========================
# MAIN LOOP
# =========================
while True:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(URL, headers=headers)

        if "NOTIFY ME" in r.text:
            print("Still out of stock")
            in_stock_last_time = False

        else:
            print("IN STOCK!!!")

            if not in_stock_last_time:
                send_telegram("🚨 HMT WATCH IS IN STOCK! BUY NOW!")
                in_stock_last_time = True

    except Exception as e:
        print("Error:", e)

    time.sleep(10)
