from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests
import json

color0 = "#444466"
color1 = "#feffff"
color2 ="#6f9fbd"

background = "#484f60"

window = Tk()
window.title('')
window.geometry('320x350')
window.configure(bg=background)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)

top_frame = Frame(window, width=320,height=50,bg=color1, pady=0,padx=0, relief='flat')
top_frame.grid(row=1,column=0)

bottom_frame = Frame(window, width=320,height=300,bg=background, pady=0,padx=0, relief='flat')
bottom_frame.grid(row=2,column=0,sticky=NW)

def info():

    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'
    response = requests.get(api_link)
    data = response.json()

    value_usd = float(data['USD'])
    value_format_usd = "$ {:,.3f}".format(value_usd)
    l_p_usd['text'] = value_format_usd

    value_euro = float(data['EUR'])
    value_format_euro = "€ {:,.3f}".format(value_euro)
    l_p_euro['text'] = value_format_euro

    value_real = float(data['BRL'])
    value_format_real = "R$ {:,.3f}".format(value_real)
    l_p_real['text'] = value_format_real

    value_kwanzas = float(data['AOA'])
    value_format_kwanzas = "Kz {:,.3f}".format(value_kwanzas)
    l_p_kwanzas['text'] = value_format_kwanzas

    bottom_frame.after(1000,info)


image = Image.open('images/ic_bitcoin.png')
image = image.resize((30,30),Image.Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)

l_icon = Label(top_frame, image=image,bg=color1,compound=LEFT,relief=FLAT)
l_icon.place(x=10,y=10)

l_title = Label(top_frame, text='Bitcoin Price Tracker',bg=color1, fg=color2,relief=FLAT, anchor='center',font=("Arial 18"))
l_title.place(x=50,y=5)


l_p_usd = Label(bottom_frame, text='', width=14,bg=background, fg=color1,relief=FLAT, anchor='center',font=("Arial 20"))
l_p_usd.place(x=0,y=50)

l_p_euro = Label(bottom_frame, text='', width=14,bg=background, fg=color1,relief=FLAT, anchor='center',font=("Arial 12"))
l_p_euro.place(x=10,y=130)

l_p_real = Label(bottom_frame, text='', width=14,bg=background, fg=color1,relief=FLAT, anchor='center',font=("Arial 12"))
l_p_real.place(x=0,y=160)

l_p_kwanzas = Label(bottom_frame, text='', width=14,bg=background, fg=color1,relief=FLAT, anchor='center',font=("Arial 12"))
l_p_kwanzas.place(x=0,y=190)



info()

window.mainloop()