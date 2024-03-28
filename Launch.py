from Bot_Details import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Initiate the Client
app = Client("xyz", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

text = "hi"
text_button = [
    [
        InlineKeyboardButton("next", callback_data="go_next")
    ]
]

@app.on_message(filters.command('launch') & filters.private)
async def launch(bot, message):
    await message.reply(
        text=text,
        reply_markup=InlineKeyboardMarkup(text_button)
    )

@app.on_callback_query()
async def callback_query(client, callbackQuery):
    if callbackQuery.data == "go_next":
        await callbackQuery.message.edit_media(media="BAACAgUAAxkBAAPWZgKNra82bPHl-IL9-4HPcg8uGrkAAqERAAKSdRhUrVsfGHzt9YIeBA")

app.run()
