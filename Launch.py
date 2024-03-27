# Import all necessary modules
 
from Bot_Details import *
from pyrogram import Client, filters
import asyncio


#Initiate the Client

app = Client("Launch", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command('launch')&filters.private)
async def launch(bot,message) :
    await bot.send_video(message.chat.id,"BAACAgUAAxkBAAPWZgKNra82bPHl-IL9-4HPcg8uGrkAAqERAAKSdRhUrVsfGHzt9YIeBA")

app.run()

