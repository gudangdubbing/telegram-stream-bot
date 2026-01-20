from pyrogram import Client, filters

api_id = 36913469
api_hash = "6e3485759824023ab5b303e4c7271948"
bot_token = "8564107690:AAFt_ACrM6atWoi6jILHqi64sGi0LOKA0BM"

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
