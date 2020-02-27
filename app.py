import json
from tkinter import *
master = Tk() 
Label(master, text='Enter the word to be search').grid(row=0)

e1 = Entry(master) 
 
e1.grid(row=0, column=1) 
 
mainloop() 
from difflib import get_close_matches
store=json.load(open("data.json"))
words=input("Enter words to be search:")
if words in store.keys():
    print(store[words])
elif len(get_close_matches(words,store)) > 0:
    a=input("Are you want to looking for that word Enter YES else Enter NO:")
    if a == "YES":
        print(get_close_matches(words,store.keys()))
    elif a == "NO":
        print("Word not Found")
