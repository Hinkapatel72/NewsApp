class Preferences():
    def __init__(self, preferences):
        '''
        preferences: comma separated string of news preferences.
                     example: "business,sports,politics"
        '''
        self.preferences = preferences

    def get_preferences(self):
        return self.preferences
