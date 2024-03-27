# Import all necessary modules
 
from Bot_Details import *
from pyrogram import Client, filters
import asyncio

#Initiate the Client

app = Client("Start_Command_pm", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

#Define a handler for the /start command in bot pm

@app.on_message(filters.command('start')&filters.private)
async def start (bot, message):
    await message.reply_photo(photo="https://telegra.ph/file/51ddcb40c9192d6ceb334.jpg", caption ="⭐️ __**Hello, Welcome⭐️\n\n🌟Send /launch to launch the game🌟**__")

app.run()