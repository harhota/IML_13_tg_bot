# emelis_friend 
This is an example of a toy Telegram chatbot using the OpenAI API.
The bot can be used locally or deployed on a cloud server as Docker container.

## Prerequisites
### Telegram Bot Token
You need to obtain a token for access to your bot's HTTP API:

1. Find the `@BotFather` bot in Telegram
2. Send him the `/newbot` command
3. Enter the project name and bot name
4. Copy the received token
5. Add recieved token to .env : ```echo "TELEGRAM_BOT_TOKEN=your_key" > .env```
	

### Open AI Token
You need to obtain an Open AI token. 

1. Please follow the instruction provided by openai to receive your token.
2. Add recieved token to .env: ```echo "OPENAI_API_KEY=your_key" >> .env``

## Project Structure

```
telegram_chatbot_boilerplate/
│
├── config/
│   ├─── openai_client.py
│   ├─── telegram_bot.py
│   └─── tokens.py
│
├── handlers/
│   ├── __init__.py
│   ├── command_handlers.py
│   └── message_handlers.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── app.py
├── Dockerfile
├── .env
└── requirements.txt
```

acknowledgment: this example was ispired by https://github.com/dimadem/telegram_chatbot_boilerplate/tree/main
