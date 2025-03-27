from pyrogram import Client, filters

app = Client("my_bot", api_id=25637343, api_hash="70fb79a89ec2d30cab05704e817e5be6", bot_token="BOT_TOKEN")

@app.on_message(filters.photo)
async def get_photo_id(client, message):
    file_id = message.photo.file_id
    await message.reply(f"Photo File ID: `{file_id}`")
    print(f"Photo File ID: {file_id}")

app.run()
