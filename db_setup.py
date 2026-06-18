import sqlite3

def setup():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # යූසර්ගේ නම, බැලන්ස් එක සහ තත්ත්වය (Status) ගබඩා කරන ටේබල් එක
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, balance REAL DEFAULT 0, status TEXT)''')
    conn.commit()
    conn.close()
    print("✅ Database එක සාර්ථකව හැදුවා!")

if __name__ == '__main__':
    setup()