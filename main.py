from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Mesajı oxuyuruq
    msg = request.form.get("Body")

    # Cavab göndəririk
    resp = MessagingResponse()
    resp.message(f"Salam! Sizin mesajınız: {msg}")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
