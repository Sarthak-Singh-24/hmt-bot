import requests
import time

# ====== YOUR DETAILS ======
BOT_TOKEN = "8685765922:AAFWXBKbkVr_Nh0vrtMczUDMMA0o7vEQ9rA"
CHAT_ID = "2136328173"   # your chat id

URL = "https://www.hmtwatches.in/product_details?id=155"

# ====== TELEGRAM FUNCTION ======
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

# ====== CHECK FUNCTION ======
def check_stock():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers)

    if "Out of Stock" not in r.text:
        print("IN STOCK!!!")
        send_telegram("🚨 HMT WATCH IN STOCK!!!")
    else:
        print("Still out of stock")

# ====== RUN ======
send_telegram("✅ Bot is running")

while True:
    check_stock()
    time.sleep(10)
