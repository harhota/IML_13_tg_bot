import json

from telegram import Update,KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def start_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # updateable object
    update_obj = json.dumps(update.to_dict(), indent=4)

    reply = "*update object*\n\n" + "```json\n" + update_obj + "\n```"

    # route a reply to Telegram
    await update.message.reply_text(reply, parse_mode="Markdown")

    print("assistant:", reply)
