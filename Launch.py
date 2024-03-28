# Import all necessary modules
 
from Bot_Details import *
from pyrogram import Client, filters
import asyncio


#Initiate the Client

app = Client("xyz", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

text = "hi"
text_button = [
    [
        InlineButtonKeyboard("next",callback_data= "go_next")
    ]
]

@app.on_message(filters.command('launch')&filters.private)
async def launch(bot,message) :
    await message.reply(
        text = text,
        reply_markup = text_button
    )

@app.on_callback_query()
def callback_query(client, callbackQuery):
    if CallbackQuery.data == "go_next":
        await CallbackQuery.edit.message_video(message.chat.id,"BAACAgUAAxkBAAPWZgKNra82bPHl-IL9-4HPcg8uGrkAAqERAAKSdRhUrVsfGHzt9YIeBA")

app.run()

