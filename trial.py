from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import json
import asyncio


app = Client("trail", api_id=20058505, api_hash="c6416428be72db3174999c1740524b88" bot_token="7017225800:AAH87ICUBwfIEvlyQhOC7jfiRbjtMC5A6wY")


@app.on_message(filters.command("walk"))
async def walk_command_handler(client, message):
    x = random.randint(1, 808)
    level = random.randint(1, 85)
    with open('pokedex.json') as f:
        data = json.load(f)
    y = x + 1
    if y < 100:
        if y < 10:
            fname = "00" + str(y)
        else:
            fname = "0" + str(y)
    else:
        fname = str(y)
    file_path = f"images/{fname}.png"
    caption = f"A wild {data[x]['name']['english']} (Lvl. {level}) has appeared"
    await message.reply_photo(
        photo=file_path,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Catch", callback_data=f"catch;{level};{data[x]['base']['Speed']};{data[x]['name']['english']}"),
                    InlineKeyboardButton("Pokedex", callback_data="Pokedex")
                    ]
            ]
        )
    )




@app.on_callback_query()
async def character_cards(client, event):
    data = event.data.decode()
    if "Catch" in data:
        lmao = data.split(";")
        b = await client.edit_message(event.message.chat.id, event.message.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Catch", "fled"), InlineKeyboardButton("Pokedex", "pokedex")]]))
        t = await client.send_message(event.message.chat.id, "Choose a Pokeball to throw", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Regular", f"ball;regular;{lmao[1]};0;{lmao[2]};{lmao[3]}"),
             InlineKeyboardButton("Great", f"ball;great;{lmao[1]};0;{lmao[2]};{lmao[3]}"),
             InlineKeyboardButton("Ultra", f"ball;ultra;{lmao[1]};0;{lmao[2]};{lmao[3]}")],
            [InlineKeyboardButton("Level", f"ball;level;{lmao[1]};0;{lmao[2]};{lmao[3]}"),
             InlineKeyboardButton("Repeat", f"ball;repeat;{lmao[1]};0;{lmao[2]};{lmao[3]}"),
             InlineKeyboardButton("Quick", f"ball;quick;{lmao[1]};0;{lmao[2]};{lmao[3]}")]
        ]))
        await asyncio.sleep(1200)
        a = await client.get_messages(event.message.chat.id, t.message_id)
        print(a)
        if "caught" in a.text:
            pass
        elif "CRY" in a.text:
            pass
        else:
            await client.edit_message(event.message.chat.id, t.message_id, "THE POKEMON RAN AWAY")

@app.on_callback_query(filters.regex("^fled$"))
async def character_cards_fled(client, event):
    print("Fled")
    await event.answer("THIS POKE HAS ALREADY FLED")

@app.on_callback_query()
async def character_cards_ball(client, event):
    data = event.data.decode()
    if "ball" in data:
        a = data.split(";")
        if a[1] == "regular":
            x = 100 * 1
        elif a[1] == "great":
            x = 100 * 1.5
        elif a[1] == "ultra":
            x = 100 * 2
        elif a[1] == "level":
            d = 3 - (int(a[2]) - 1) // 10 * 0.1
            x = 100 * d
        elif a[1] == "repeat":
            x = 100 * (1 if a[3] == "0" else 3)
        else:
            x = 100 * (1 + ((int(a[4]) - 1) // 10) * 0.1)
        print(x)
        numberList = ["Fled", "Caught", "Re"]
        rate = random.choices(numberList, weights=(20, int(x), 80), k=1)
        rate1 = random.choices(numberList, weights=(20, int(x), 80), k=1)
        rate2 = random.choices(numberList, weights=(20, int(x), 80), k=1)
        rate3 = random.choices(numberList, weights=(20, int(x), 80), k=1)
        print(rate, rate1, rate2, rate3)
        butt = [
            [InlineKeyboardButton("Regular", f"ball;regular;{a[2]};1;{a[4]};{a[5]}"),
             InlineKeyboardButton("Great", f"ball;great;{a[2]};1;{a[4]};{a[5]}"),
             InlineKeyboardButton("Ultra", f"ball;ultra;{a[2]};1;{a[4]};{a[5]}")],
            [InlineKeyboardButton("Level", f"ball;level;{a[2]};1;{a[4]};{a[5]}"),
             InlineKeyboardButton("Repeat", f"ball;repeat;{a[2]};1;{a[4]};{a[5]}"),
             InlineKeyboardButton("Quick", f"ball;quick;{a[2]};1;{a[4]};{a[5]}")]
        ]
        await client.edit_message(event.message.chat.id, event.message.message_id, "You used a {} ball.".format(a[1].capitalize()))
        await asyncio.sleep(2)
        if rate == ["Caught"]:
            await client.edit_message(event.message.chat.id, event.message.message_id, "You used a {} ball. ✧".format(a[1].capitalize()))
            await asyncio.sleep(2)
            if rate1 == ["Caught"]:
                await client.edit_message(event.message.chat.id, event.message.message_id, "You used a {} ball. ✧✧".format(a[1].capitalize()))

await asyncio.sleep(2)
                if rate2 == ["Caught"]:
                    await client.edit_message(event.message.chat.id, event.message.message_id, "You used a {} ball. ✧✧✧".format(a[1].capitalize()))
                    await asyncio.sleep(2)
                    if rate3 == ["Caught"]:
                        await client.edit_message(event.message.chat.id, event.message.message_id, "You used a {} ball. ✦✦✦".format(a[1].capitalize()))
                        await asyncio.sleep(2)
                        y = my_function()
                        print(y)
                        with open('pokedex.json') as f:
                            data = json.load(f)
                        print("rdtfyguhij")
                        for k in range(0, 809):
                            if data[k]["name"]["english"] == a[5]:
                                tipe = data[k]["type"]
                        text = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(
                            event.sender_id, 1, a[5], "NULL", y[-1], a[2], "-", "-", tipe, "NULL", y[0], y[1], y[2],
                            y[3], y[4], y[5], 0, 0, 0, 0, 0,

app.run()