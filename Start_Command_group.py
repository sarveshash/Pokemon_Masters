# Import all necessary modules
 
from Bot_Details import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Initiate the Client

app = Client("Start_Command_group", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

#Define a handler for the /start command in group

@app.on_message(filters.command("start") & filters.group)
async def start_command_group(client, message):

    # Create an inline keyboard with a button to start a private chat with the bot

    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Start", url="t.me/PokedemoBot?start=start")]])
    
    # Send the message with the inline keyboard

    await message.reply_photo(photo="https://telegra.ph/file/c2615efafab5394f2d198.jpg", caption ="__**🚫Oh ! An error occurred !🚫\n\n🔹Try sending /start in the private by pressing the button below ! 🔹**__", reply_markup=keyboard)

# Define a callback query handler to handle button clicks
    
@app.on_callback_query()
async def callback_query_handler(client, callback_query):

    # Check if the callback data is "start_chat"

    if callback_query.data == "start_chat":

        # Send the /start command to the bot in a private chat
        
        await callback_query.message.chat.send_message("/start")



# Start the bot     

app.run()