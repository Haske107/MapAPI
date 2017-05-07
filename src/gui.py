from Tkinter import *
import json, urllib
from urllib import urlencode
from googlemaps import Client
import webbrowser

class Application(Frame):


    def say_hi(self):
        gmaps = Client('AIzaSyD0AJQRoThLlugn1lW_TgYhRBtRON34LDA')
        start = self.E1.get()
        finish = self.E2.get()

        url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
                    ('origin', start),
                    ('destination', finish)
         ))
        ur = urllib.urlopen(url)
        result = json.load(ur)
        for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
            j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
            self.list1.insert(0,j)
        #webbrowser.open('https://www.google.com/maps/dir/'+start+'/' + finish)


    def createWidgets(self):
        self.E1 = Entry(self, bd =5)
        self.E1.pack(side = RIGHT)
        self.L1 = Label(self, text="To:")
        self.L1.pack( side = RIGHT)
        self.E2 = Entry(self, bd =5)
        self.E2.pack(side = RIGHT)
        self.L2 = Label(self, text="From:")
        self.L2.pack( side = RIGHT)
        self.list1 = Listbox(self)
        self.list1.pack()
        self.list1.config(width=100)
        self.hi_there = Button(self)
        self.hi_there["text"] = "Get Results",
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack()
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack()


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
