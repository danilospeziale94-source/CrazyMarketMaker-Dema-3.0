import os
import telebot
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🟢 Affiliazione PU Prime", callback_data="affiliazione"))
    markup.add(InlineKeyboardButton("🛒 Acquista Pacchetto DEMA 3.0 - 299€", callback_data="acquista"))
    markup.add(InlineKeyboardButton("📥 Guida Installazione", callback_data="install"))
    markup.add(InlineKeyboardButton("❓ FAQ", callback_data="faq"))
    markup.add(InlineKeyboardButton("💬 Contattami in Privato", callback_data="contact"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = """
<b>👋 Benvenuto nel Bot Ufficiale DEMA 3.0</b>

Qui gestisco automaticamente l'accesso al sistema completo:
• Indicatore Crazy Market Maker
• EA Semiautomatico
• Copy Trading

Per procedere devi prima affiliarti a <b>PU Prime</b>.
"""
    bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "affiliazione":
        text = """
<b>🟢 AFFILIAZIONE PU PRIME</b>

Clicca qui per registrarti:
👉 <a href="https://puvip.co/la-partners/B8gYmnJT">REGISTRATI ORA</a>

<b>Codice di riferimento:</b> <code>B8gYmnJT</code>

Dopo aver completato la registrazione e la verifica, torna qui e clicca su "Acquista Pacchetto".
"""
    
    elif call.data == "acquista":
        text = """
<b>🛒 ACQUISTA PACCHETTO DEMA 3.0</b>

Prezzo: <b>299€</b> (pagamento unico)

<b>Effettua il bonifico a:</b>

IBAN: <code>IT04M0306902506100000005672</code>
Intestato a: De martino Gennaro

Una volta fatto il bonifico, scrivi in privato a:
• @crazymarketmakerEA
• @Demafranzfx

Ti daremo accesso immediato al sistema completo.
"""

    elif call.data == "install":
        text = "Guida all'installazione (TradingView + futura MT5) in arrivo."

    elif call.data == "faq":
        text = "FAQ e informazioni dettagliate in arrivo."

    else:  # contact
        text = """
<b>💬 Contatto Privato</b>

Scrivi direttamente a:
@crazymarketmakerEA
oppure
@Demafranzfx

Solo dopo aver completato affiliazione + bonifico.
"""

    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=main_menu())

print("🚀 Bot DEMA 3.0 avviato con successo!")
bot.infinity_polling()