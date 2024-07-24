from telegram import Update
from config.openai_client import client 

async def chatgpt_reply(update: Update, context):
    # user query
    text = update.message.text

    # open ai prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text + """You are a kind and nice woman.
                   Yoou are a professional machine learning researcher.
                   You have own startup company - Evidently.AI - this is a monitoring tool
                   that is supposed to be built on top of ML solution."""}],
        max_tokens=1024,
        temperature=0.5,
    )

    # open ai response
    reply = response.choices[0].message.content.strip()

    # route a response to Telegram
    await update.message.reply_text(reply)   
    
    print("user:", text)
    print("assistant:", reply)
