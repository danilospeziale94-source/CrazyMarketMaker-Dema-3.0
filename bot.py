import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram import F

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Manca TELEGRAM_BOT_TOKEN nel file .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🟢 Copy Trading PU Prime", callback_data="copy_trading")],
        [InlineKeyboardButton(text="🛒 Acquista Pacchetto Indicatori", callback_data="buy_indicators")],
        [InlineKeyboardButton(text="📥 Accedi / Installa Indicatore", callback_data="access_indicator")],
        [InlineKeyboardButton(text="❓ FAQ & Come Funziona", callback_data="faq")],
        [InlineKeyboardButton(text="💬 Parla con me", callback_data="contact")]
    ])
    return kb

def back_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Torna al Menu", callback_data="main_menu")]
    ])

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "<b>👋 Benvenuto nel Sales Bot!</b>\n\nScegli un'opzione:", 
        parse_mode="HTML",
        reply_markup=main_menu_keyboard()
    )

@dp.callback_query(F.data == "main_menu")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text("Scegli un'opzione:", reply_markup=main_menu_keyboard())
    await callback.answer()

# Altri pulsanti (per ora base)
@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    if callback.data == "copy_trading":
        await callback.message.edit_text("Link Copy Trading da inserire qui.\n\nTorna al menu.", reply_markup=back_keyboard())
    elif callback.data == "buy_indicators":
        await callback.message.edit_text("Link acquisto da inserire qui.\n\nTorna al menu.", reply_markup=back_keyboard())
    else:
        await callback.message.edit_text("Funzione in arrivo...", reply_markup=back_keyboard())
    await callback.answer()

async def main():
    print("🚀 Bot avviato con successo!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())