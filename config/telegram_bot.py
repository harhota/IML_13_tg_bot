from telegram.ext import Application 
from .tokens import TELEGRAM_BOT_TOKEN 

# A bot instance app
application = (Application.builder()
                .token(TELEGRAM_BOT_TOKEN)
                .connect_timeout(30)
                .read_timeout(30)
                .write_timeout(30)
                .build())

