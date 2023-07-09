import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


START_TEXT = """
Привет!

Я твой помощник в решении игры Wordle!
Ты можешь использовать следующие команды:

/newgame - начать новую игру
/nextword - введи следующее слово и внеси информацию о буквах (какая зеленая, какая желтая и т.п.)
/myguesses - я предложу тебе список из подходящих в твоей ситуации слов
/valid - проверка того, что твое слово существует
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=START_TEXT)


if __name__ == '__main__':
    print(alphabet)
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        exit("You should specify BOT_TOKEN in .env file!")
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()