from pyrogram import Client, filters
import os

api_id = int(os.environ.get("36913469"))
api_hash = os.environ.get("6e3485759824023ab5b303e4c7271948")
bot_token = os.environ.get("8564107690:AAFt_ACrM6atWoi6jILHqi64sGi0LOKA0BM")

app = Client(
    "streambot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🤖 Bot aktif!")

app.run()
