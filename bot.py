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
    markup.add(InlineKeyboardButton("💰 2. Pagamento Pacchetto 299€", callback_data="pagamento"))
    markup.add(InlineKeyboardButton("💬 3. Contattami in Privato", callback_data="contact"))
    markup.add(InlineKeyboardButton("🌐 Sito Web Ufficiale", callback_data="sito"))
    markup.add(InlineKeyboardButton("🎟 Codici Sconto", callback_data="sconti"))
    markup.add(InlineKeyboardButton("⚠️ Disclaimer", callback_data="disclaimer"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = """
<b>👋 Benvenuto!</b>

Sono l'<b>Assistente IA Ufficiale della DEMAFRANZFX</b>.

Da qui puoi accedere alla <b>Crazy DEMA 3.0</b>.

Visita il <b>Sito Web Ufficiale</b> per acquistare i prodotti della DEMAFRANZFX.

In basso trovi i codici sconto.

Per accedere ai servizi segui i seguenti passaggi in ordine:
"""
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "affiliazione":
        text = """
<b>1. AFFILIAZIONE PU PRIME</b>

Clicca qui per registrarti:
👉 <a href="https://puvip.co/la-partners/B8gYmnJT">REGISTRATI SU PU PRIME</a>

Inserisci il codice: <b>B8gYmnJT</b>

Dopo la registrazione invia questa email a info@puprime.com:

"Hello, I want to be moved under IB 23211945
"""

    elif call.data == "pagamento":
        text = """
<b>2. PAGAMENTO PACCHETTO DEMA 3.0</b>

Importo: <b>299€</b> (pagamento unico)

Effettua il bonifico su:
IBAN: <code>IT04M0306902506100000005672</code>
Intestato a: De martino Gennaro
"""

    elif call.data == "contact":
        text = """
<b>3. CONTATTAMI IN PRIVATO</b>

Dopo aver completato affiliazione + pagamento scrivi a:
@crazymarketmakerEA
oppure
@Demafranzfx

Riceverai l’accesso completo alla Crazy DEMA 3.0
"""

    elif call.data == "sito":
        text = """
<b>🌐 SITO WEB UFFICIALE</b>

Visita il sito per acquistare tutti i prodotti DEMAFRANZFX:
👉 https://demafranzfx.com/
"""

    elif call.data == "sconti":
        text = """
<b>🎟 CODICI SCONTO</b>

• <b>CMM50</b> → Ingresso Discord
• <b>CMM300</b> → Corso Full
"""

    elif call.data == "disclaimer":
        text = """
<b>⚠️ DISCLAIMER</b>

Il trading comporta un alto rischio di perdita del capitale. 
I risultati passati non garantiscono risultati futuri. 
L'utente è l'unico responsabile delle proprie operazioni.
"""

    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=main_menu())

print("🚀 Bot DEMA 3.0 avviato con successo!")
bot.infinity_polling()
