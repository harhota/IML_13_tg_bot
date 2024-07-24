from telegram.ext import MessageHandler, CommandHandler, filters
from config.telegram_bot import application 
from handlers.message_handlers import chatgpt_reply 
from handlers.command_handlers import start_reply

# Registering a Text Message Handler
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply)
application.add_handler(message_handler)

# Registering a Command Handler
start_command_handler = CommandHandler("start", start_reply)
application.add_handler(start_command_handler)

# A bot run
application.run_polling()
