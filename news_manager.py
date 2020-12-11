import requests

class NewsManager():
    URL = "http://newsapi.org/v2/top-headlines"
    def __init__(self, api_key="99ea0040a3054a67afb333112ee40369"):
        self.authed_url = "{}?apiKey={}".format(NewsManager.URL, api_key)

    def fetch_news(self, param_dict):
        query_param_arr = []
        for k in param_dict:
            query_param_arr.append("{}={}".format(k,param_dict[k]))

        query_param_str = "&".join(query_param_arr)
        fetch_url = "{}&{}".format(self.authed_url, query_param_str)
        res = requests.get(fetch_url)
        if res.status_code == 200:
            return res.json()['articles']

        print("An error occurred while attempting to retrieve data from the API!")
        return []
