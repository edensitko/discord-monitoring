from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "WEBHOOK HERE "

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    alerts = data.get("alerts", [])

    for alert in alerts:
        # רק התראות firing נשלחות
        if alert.get("status") != "firing":
            continue

        status = alert.get("status", "firing").upper()
        summary = alert.get("annotations", {}).get("summary", "אין תקציר")
        description = alert.get("annotations", {}).get("description", "אין תיאור")
        instance = alert.get("labels", {}).get("instance", "לא ידוע")
        emoji = "🚨התראה"
        message = f"**[{emoji}] {summary}**\n{description}\n📡 `{instance}`"

        res = requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
        if res.status_code != 204:
            print("שגיאה בשליחה לדיסקורד:", res.text)

    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
