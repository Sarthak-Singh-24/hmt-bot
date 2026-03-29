import requests
import time

URL = "https://www.hmtwatches.in/product_overview?id=eyJpdiI6IlhnZS9EemVhTXJnU09aL1VtSndnWUE9PSIsInZhbHVlIjoiSGdCM3l3a2RGQTNhZUxSTnhpUEtjZz09IiwibWFjIjoiZThiZWQyNGMzNjA4MThmZDRhYmYxNDFlYTE1ZTU2YTAxY2NlNWNlNGJhNjZmNzQ0OWZkMjA4OTcyYzQ3ZmY3NyIsInRhZyI6IiJ9"

BOT_TOKEN = "8685765922:AAFWXBKbkVr_Nh0vrtMczUDMMA0o7vEQ9rA"
CHAT_ID = "2136328173"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

print("Starting container...")

send_telegram("✅ Bot is running")

in_stock_last_time = False

while True:
    try:
        r = requests.get(URL)

        # IMPORTANT FIX: detect ADD TO CART (means IN STOCK)
        if "ADD TO CART" in r.text:
            print("IN STOCK!!!")

            if not in_stock_last_time:
                send_telegram("🔥 HMT WATCH IS IN STOCK! BUY NOW!")
                in_stock_last_time = True

        else:
            print("Still out of stock")
            in_stock_last_time = False

    except Exception as e:
        print("Error:", e)

    time.sleep(10)
