import sys
from tkinter import *
import tkMessageBox
from preferences import Preferences
import database_utils

# create root window
root = Tk()
root.config(bg="#add0ed")

class PreferenceWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.PrefB = StringVar()
        self.PrefSp = StringVar()
        self.PrefA = StringVar()
        self.PrefU = StringVar()
        self.PrefBbc = StringVar()
        self.PrefBtcoin = StringVar()
        self.__createWidgets()

    def destroy(self):
        self.left_frame.destroy()
        self.right_frame.destroy()
        self.tool_bar.destroy()
        Frame.destroy(self)

    def __save_preferences(self):
        # get selected buttons.
        bus = self.PrefB.get()
        spo = self.PrefSp.get()
        apple = self.PrefA.get()
        usa = self.PrefU.get()
        bbc = self.PrefBbc.get()
        bitcoin = self.PrefBtcoin.get()
        pref = []
        if bus:
            pref.append(bus)
        if spo:
            pref.append(spo)
        if apple:
            pref.append(apple)
        if usa:
            pref.append(usa)
        if bbc:
            pref.append(bbc)
        if bitcoin:
            pref.append(bitcoin)

        # make comma separated list from that.
        pref_str = ",".join(pref)
        pref = Preferences(pref_str)

        database_utils.save_preferences(pref)
        self.quit()

    def __createWidgets(self):

        left_frame = Frame(root, width=400, height=800, bg='grey')
        left_frame.grid(row=0, column=0, padx=100, pady=50)

        right_frame = Frame(root, width=350, height=200, bg='grey')
        right_frame.grid(row=0, column=1, padx=30, pady=5)

        self.left_frame = left_frame
        self.right_frame = right_frame

        Label(left_frame, text="Please Select Your Preference", relief=RAISED, font=('Helvetica', 22, 'bold')).grid(row=0, column=0, padx=25, pady=25)

        tool_bar = Frame(left_frame, width=280, height=285, bg='grey')
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        self.tool_bar = tool_bar

        Checkbutton(tool_bar, text="Business", variable = self.PrefB, onvalue = "business", offvalue = "", font=('Times', 18, 'italic')).grid(row=1, column=0, padx=5, pady=3, ipadx=10)

        Checkbutton(tool_bar, text="Sports", variable = self.PrefSp, onvalue = "sports", offvalue = "", font=('Times', 18, 'italic')).grid(row=2, column=0, padx=5, pady=3, ipadx=10)

        Checkbutton(tool_bar, text="Apple", variable = self.PrefA, onvalue = "apple", offvalue = "", font=('Times', 18, 'italic')).grid(row=3, column=0, padx=5, pady=3, ipadx=10)

        Checkbutton(tool_bar, text="USA News", variable = self.PrefU, onvalue = "us", offvalue = "", font=('Times', 18, 'italic')).grid(row=4, column=0, padx=5, pady=3, ipadx=10)

        Checkbutton(tool_bar, text="BBC News", variable = self.PrefBbc, onvalue = "trump", offvalue = "", font=('Times', 18, 'italic')).grid(row=5, column=0, padx=5, pady=3, ipadx=10)

        Checkbutton(tool_bar, text="Bitcoin", variable = self.PrefBtcoin, onvalue = "bitcoin", offvalue = "", font=('Times', 18, 'italic')).grid(row=6, column=0, padx=5, pady=3, ipadx=10)

        Button(tool_bar, text="Go to Next Page", command=self.__save_preferences, font=('Helvetica', 20, 'bold')).grid(row=8, column=0, padx=30, pady=30, sticky='w'+'e'+'n'+'s')


        Label(right_frame, text="Here you find all latest news from your selected preferences, please go ahead and select your preferences first!", relief=RAISED, font=('Helvetica', 20, 'bold'), wraplength=250, justify="center").grid(row=0, column=0, padx=25, pady=25)
        Label(right_frame, text="There is a direct connection between what you are watching, reading, and listening to all day, and how you feel. Your energy levels, your mood, your ambition.", font=('Times', 18, 'italic'), wraplength=250, justify="center").grid(row=1, column=0, padx=25, pady=25)
