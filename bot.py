from pyrogram import Client, filters

api_id = 123456
api_hash = "API_HASH"
bot_token = "BOT_TOKEN"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("✅ Bot aktif! Siap lanjut.")

app.run()
