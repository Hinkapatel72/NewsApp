import os
from preference_window import PreferenceWindow
from preferences import Preferences
from news_window import NewsWindow
import database_utils


def first_time_launch():
    return not os.path.exists(database_utils.DATABASE_FILE)

def main():
    if first_time_launch():
        database_utils.create_news_preference_table()
        preference_window = PreferenceWindow()
        preference_window.master.title("News application")
        preference_window.master.geometry("900x700")
        preference_window.mainloop()
        preference_window.destroy()

    preferences = database_utils.get_preferences()

    '''
     - Load main news window.
     - news window uses new api file to use features like fetching news for category.
    '''
    news_window = NewsWindow(preferences)
    news_window.master.title("News application")
    news_window.master.geometry("900x600")
    news_window['background']='#add0ed'
    news_window.mainloop()



if __name__ == "__main__":
    main()
