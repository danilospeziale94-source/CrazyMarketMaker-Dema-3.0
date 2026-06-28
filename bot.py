import os
import telebot
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🟢 1. Affiliazione PU Prime", callback_data="affiliazione"))
    markup.add(InlineKeyboardButton("💰 2. Pagamento Pacchetto", callback_data="pagamento"))
    markup.add(InlineKeyboardButton("💬 3. Contattami in Privato", callback_data="contact"))
    markup.add(InlineKeyboardButton("📊 Abbonamento Mensile 150€", callback_data="mensile"))
    markup.add(InlineKeyboardButton("📋 Prezzi Extra", callback_data="prezzi"))
    markup.add(InlineKeyboardButton("⚠️ Disclaimer", callback_data="disclaimer"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = """
<b>👋 Benvenuto nel Bot Ufficiale DEMA 3.0</b>

Sito Ufficiale: <a href="https://demafranzfx.com/">demafranzfx.com</a>

Per accedere ai servizi segui questi passi in ordine:
"""
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "affiliazione":
        text = """
<b>🟢 1. AFFILIAZIONE PU PRIME</b>

1. Registrati qui:
👉 <a href="https://puvip.co/la-partners/B8gYmnJT">REGISTRATI SU PU PRIME</a>

2. Inserisci codice: <b>B8gYmnJT</b>

3. Completa verifica identità.

<b>Dopo la registrazione invia questa email:</b>

A: info@puprime.com

Oggetto: Request to be moved under IB

Testo:
Hello, I want to be moved under IB CMM50

Una volta completata l'affiliazione, procedi al pagamento.
"""

    elif call.data == "pagamento":
        text = """
<b>💰 2. PAGAMENTO PACCHETTO DEMA 3.0</b>

Importo: <b>299€</b> una tantum

Bonifico a:
IBAN: <code>IT04M0306902506100000005672</code>
Intestato a: De martino Gennaro

Dopo il bonifico vai al punto 3.
"""

    elif call.data == "contact":
        text = """
<b>💬 3. CONTATTAMI IN PRIVATO</b>

Hai completato affiliazione + bonifico?

Scrivi in privato a:
@crazymarketmakerEA
o
@Demafranzfx

Riceverai subito le istruzioni per accedere ai servizi.
"""

    elif call.data == "mensile":
        text = """
<b>📊 ABBONAMENTO MENSILE 150€</b>

Accesso completo alle nostre vendite esclusive.

Ogni giorno avrai:
✅ Operatività personale con entry, SL e TP
✅ Analisi su XAUUSD, EUR/USD, Bitcoin
✅ Video esclusivi
✅ Ciclica algoritmica proprietaria

Per attivare scrivi in privato.
"""

    elif call.data == "prezzi":
        text = """
<b>📋 PREZZI EXTRA</b>

• CMM50 → Ingresso Discord
• CMM300 → Corso Full

Per info scrivi in privato.
"""

    elif call.data == "disclaimer":
        text = """
<b>⚠️ DISCLAIMER</b>

Il trading comporta alto rischio di perdita di capitale.
I risultati passati non garantiscono risultati futuri.
Tutti gli strumenti hanno scopo educativo.
L'utente è l'unico responsabile delle proprie operazioni.
"""

    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=main_menu())

print("🚀 Bot DEMA 3.0 avviato con successo!")
bot.infinity_polling()