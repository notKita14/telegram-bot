from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = os.getenv("8823071278:AAHWYpDY6fVb4d4dVLwgTesLeByT6oZCRc0")
YOUR_ID = int(os.getenv("1446366156"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши сообщение — оно отправится владельцу."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text

    message = (
        f"Новое сообщение\n\n"
        f"Имя: {user.full_name}\n"
        f"Username: @{user.username}\n"
        f"ID: {user.id}\n\n"
        f"Сообщение:\n{text}"
    )

    await context.bot.send_message(
        chat_id=YOUR_ID,
        text=message
    )

    await update.message.reply_text(
        "Сообщение отправлено."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
)

app.run_polling()
