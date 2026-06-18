from telethon import TelegramClient, events
import sqlite3

API_ID = 27361394
API_HASH = 'b021841f18b1effa52bf577dd5bc6084'
BOT_TOKEN = '8965559029:AAGuJ2_T_a166EqspZtLYJiiEB_WwgVzgXQ'

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("සාදරයෙන් පිළිගනිමු! ලොග් වීමට /login [username] [password] ලෙස ටයිප් කරන්න.")

@bot.on(events.NewMessage(pattern='/login'))
async def login(event):
    # event එකෙන් message එක වෙන් කරගන්නවා
    msg = event.message
    args = msg.text.split()
    if len(args) < 3:
        await event.reply("වැරදියි! /login [username] [password] ලෙස ටයිප් කරන්න.")
        return
    
    username, password = args[1], args[2]
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # database එකට data ඇතුලත් කරනවා
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    await event.reply(f"✅ සාර්ථකයි {username}! ඔබ දැන් ලොග් වී ඇත.")

print("🚀 බොට් ක්‍රියාත්මකයි...")
bot.run_until_disconnected()