import tkinter as tk
import json
from difflib import get_close_matches
from tkinter import messagebox
data = json.load(open("data.json"))
screen=tk.Tk()
screen.title("Dict 2.0")
#screen.configure(background="crimson")
screen.geometry('500x500')
tk.Label(text="COLLINS", bg = "crimson",fg="black" ,font =("Arial Narrow",15,'bold'),height=2).pack()
tk.Label(text="").pack()
tk.Label(text="").pack()
word = tk.StringVar()
tk.Entry(bd=3 ,font =("Arial Narrow",12), highlightcolor="light blue" ,width=35,textvariable=word).pack()
tk.Label(text="").pack()
t = tk.Message(bg="pink", text="")
def translate(w):


    str1 = w
    str2 = str1.lower()
    if str2 in json.load(open("data.json")):
        output = data[str2]
        t.configure(fg="black", bd=1, font=("Arial Narrow", 13), width=600,  text=output,cursor="dot",relief="raised")
        t.pack()

    elif len(get_close_matches(str2, data.keys())) > 0:
        rly=tk.messagebox.askyesno("Dict 2.0", "Did you mean %s instead? " % get_close_matches(str2, data.keys())[0])

        if rly is True :
            output1 = data[get_close_matches(str2, data.keys())[0]]
            t.configure(fg="black", bd=1, font=("Arial Narrow", 13),width=600,  text=output1,cursor="dot",relief="raised")
            t.pack()
        else :
            tk.messagebox.showinfo("Dict 2.0","Sorry the word does not exist")
    else:
        tk.messagebox.showinfo("Dict 2.0", "Please check the word you have entered")
tk.Button(text="SEARCH", font=("Arial Narrow", 12), command=lambda :translate(word.get())).pack()
tk.Label(text="").pack()
tk.Label(text="").pack()
screen.mainloop()








