import os
import telebot
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🟢 Copy Trading PU Prime", callback_data="copy"))
    markup.add(InlineKeyboardButton("🛒 Acquista Pacchetto Indicatori", callback_data="buy"))
    markup.add(InlineKeyboardButton("📥 Accedi / Installa Indicatore", callback_data="install"))
    markup.add(InlineKeyboardButton("❓ FAQ", callback_data="faq"))
    markup.add(InlineKeyboardButton("💬 Parla con me", callback_data="contact"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
        "<b>👋 Benvenuto nel Sales Bot!</b>\n\nScegli un'opzione sotto:", 
        parse_mode='HTML', 
        reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "copy":
        bot.edit_message_text("Link Copy Trading PU Prime da inserire qui.", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    elif call.data == "buy":
        bot.edit_message_text("Link acquisto pacchetto da inserire qui.", call.message.chat.id, call.message.message_id, reply_markup=main_menu())
    else:
        bot.edit_message_text("Funzione in arrivo...", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

print("🚀 Bot avviato!")
bot.infinity_polling()