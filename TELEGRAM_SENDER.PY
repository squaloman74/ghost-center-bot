import os
import requests


# Puoi impostare queste variabili come variabili d'ambiente
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "INSERISCI_IL_TUO_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "INSERISCI_CHAT_ID")


def send_telegram_message(text):
    """
    Send a Telegram message using a bot token and chat ID.
    """

    if TELEGRAM_BOT_TOKEN.startswith("INSERISCI") or TELEGRAM_CHAT_ID.startswith("INSERISCI"):
        # Se non hai ancora configurato il token, non blocchiamo la pipeline
        print("⚠️ Telegram non configurato. Messaggio non inviato.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return True
    except Exception as e:
        raise RuntimeError(f"Telegram message failed: {str(e)}")

