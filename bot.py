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

# Send startup message
send_telegram("✅ Bot is running (final version)")

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

        # ✅ Correct detection logic
        if "ADD TO CART" in r.text:
            print("IN STOCK!!!")

            # send only once
            if not in_stock_last_time:
                send_telegram("🚨 HMT WATCH IS IN STOCK! BUY NOW!")
                in_stock_last_time = True

        else:
            print("Still out of stock")
            in_stock_last_time = False

    except Exception as e:
        print("Error:", e)

    time.sleep(10)
