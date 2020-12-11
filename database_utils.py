from preferences import Preferences
import sqlite3

DATABASE_FILE = "newsapp.db"

def create_news_preference_table():
    conn = sqlite3.connect('newsapp.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS NewsPreference')

    cur.execute('CREATE TABLE NewsPreference(preferences TEXT)')
    conn.commit()
    conn.close()

def get_preferences():
    conn = sqlite3.connect('newsapp.db')
    cur = conn.cursor()
    cur.execute('SELECT * from NewsPreference')
    p_row = cur.fetchone()
    p = Preferences(p_row[0])
    conn.close()
    return p


def save_preferences(preferences):
    conn = sqlite3.connect('newsapp.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO NewsPreference(preferences) VALUES(?)", (preferences.get_preferences(),))
    conn.commit()
    conn.close()
