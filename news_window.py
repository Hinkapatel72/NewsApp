import urllib
from Tkinter import *
import requests
import webbrowser
from PIL import ImageTk,Image
from urlparse import urlparse
from io import BytesIO
from news_manager import NewsManager
from preferences import Preferences
from functools import partial

class Article(object):

    def __init__(self, title, photo_img, description, url):
        super(Article, self).__init__()
        self._title = title
        self._photo_img = photo_img
        self._description = description
        self._url = url

    def get_title(self):
        return self._title

    def get_photo_img(self):
        return self._photo_img

    def get_description(self):
        return self._description

    def get_url(self):
        return self._url

def get_image(img_url):

    print("Image url is {}".format(img_url))
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((200,200), Image.ANTIALIAS)
    photoImg =  ImageTk.PhotoImage(img)
    return photoImg

def process_article(a):
    print("Article dic is {}".format(a))
    news_title = a.get("title", "Title Not found")
    news_description = a.get("description", "Description Not found")
    news_url = a.get("url", "URL Not found")
    image_url = a.get("urlToImage")
    if not image_url:
        image_url = "https://picsum.photos/200/200"
    photo_img = get_image(image_url)
    a_obj = Article(news_title, photo_img, news_description, news_url)
    return a_obj

def process_articles(articles):
    article_objs = []
    for a in articles:
        a_obj = process_article(a)
        article_objs.append(a_obj)
    return article_objs


class NewsWindow(Frame):
    def __fetch_news(self):
        articles = []
        for p in self.pref.get_preferences().split(","):
            d = {"q": p}
            articles.extend(self.news_manager.fetch_news(d))
        return process_articles(articles[:3])


    def __init__(self, pref, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)
        self.pref = pref
        self.news_manager = NewsManager()
        self.articles = self.__fetch_news()
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.current_article_index = 0
        self.news_frame = None
        self.__createWidgets()


    def load_url(self, url):
        webbrowser.open(url)

    def load_news_frame(self, article):
        if self.news_frame:
            self.news_frame.destroy()

        self.news_frame = Frame(self, bg='grey')
        self.canvas = Canvas(self.news_frame, width = 200, height = 200)
        self.news_frame.pack(fill=X)
        self.canvas.pack()
        #self.img = self.get_image(article.get("urlToImage", "https://picsum.photos/200/200"))
        self.img = article.get_photo_img()
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.lbl1 = Label(self.news_frame, text=article.get_title(), font=('Helvetica', 20, 'bold'), wraplength=500, justify="center")
        self.lbl1.pack(anchor = 'center', padx=5, pady=5)
        self.lbl2 = Label(self.news_frame, text=article.get_description(), font=('Times', 18, 'italic'), wraplength=500, justify="center")
        self.lbl2.pack(anchor = 'center', padx=5, pady=5)
        self.lbl3 = Label(self.news_frame, text="Please click the link below to read detailed news!", font=('Helvetica', 20, 'bold'), wraplength=500, justify="center")
        self.lbl3.pack(anchor = 'center', padx=5, pady=5)
        self.btn1 = Button(self.news_frame, text=article.get_url(), command=partial(self.load_url,article.get_url()), font=('Times', 18, 'italic'), wraplength=500, justify="center")
        self.btn1.pack(anchor = 'center', padx=5, pady=5)


    def load_next_news(self):
        self.load_news_frame(self.articles[self.current_article_index])
        self.current_article_index += 1
        if self.current_article_index >= len(self.articles):
            self.current_article_index = 0

    def __createWidgets(self):
        '''
        for a in self.articles[:3]:
            _ = self.get_frame(a)
        '''
        Button(self, text="Next", command=self.load_next_news, font=('Helvetica', 20, 'bold')).pack()
        self.load_next_news()
