from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_ID = os.environ.get("BOT_ID")

def send_message(text):
    requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={"bot_id": BOT_ID, "text": text}
    )

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("text", "").lower()

    if "hello" in message:
        send_message("Hey 👋 I'm online 24/7")

    elif "ping" in message:
        send_message("pong 🏓")

    elif "help" in message:
        send_message("Try: hello, ping")

    return "ok", 200

app.run(host="0.0.0.0", port=3000)
