from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from clip import clipcopy
from os import listdir
from master import infoScraper
import tkinter.font as font
import tkinter.scrolledtext as scrolledtext

bgcolor = "#000000" #black
fgcolor = "#F8FC07" #yellow


def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  profile = './profiles/' + value
  print(profile)
  openwin2(text.get(), profile)

def openwin2(_query_, _profile_):
    root.destroy()
    win2 = Tk()                     # search karne pe khulne wali window
    win2.geometry("600x500+300+130")
    win2.resizable(width=False, height=False)
    win2.configure(bg=bgcolor) 
    win2.overrideredirect(True)     
    thecontent = infoScraper(_profile_, _query_) 
    label2 = Label(win2, text= thecontent[0], bg=bgcolor, fg=fgcolor).place(x=10,y=10)
    scroll = Scrollbar(win2)
    scroll.pack(side=RIGHT, fill=Y)
    information = Text(win2, width="60",bg=bgcolor, fg=fgcolor, font="4",wrap = WORD, highlightthickness=1)
    information.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    info = thecontent[1]   
    scroll.config(command=information.yview, activebackground=bgcolor) 
    information.place(x=20, y=40)
    information.insert(tk.END, info)
    exitbutton = Button(win2, text="x", command=win2.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=557, y=1)

def addsite():
    global win3
    win3 = Tk()                         # add website karne pe khulne wali window
    win3.title('Link Analyzer(window 2)')
    win3.geometry("500x400+300+130")
    win3.configure(bg=bgcolor)
    win3.overrideredirect(True)
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=475, y=1)
    win3.resizable(width=False, height=False)
    instructions = Text(win3, width="24",bg=bgcolor, fg=fgcolor, font="4",wrap = WORD, highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=255, y=2)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    label4 = Label(win3, text="URL Sample 1", bg=bgcolor, fg=fgcolor, font="6").place(x=25,y=70)
    text4 = Entry(win3, width="35", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text4.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text4.place(x=25,y=100)
    text5 = Entry(win3, width="35", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text5.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text5.place(x=25,y=130)
    label5 = Label(win3, text="URL Sample 2", bg=bgcolor, fg=fgcolor, font="6").place(x=25,y=180)
    text6 = Entry(win3, width="35",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text6.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text6.place(x=25,y=210)
    text7 = Entry(win3, width="35",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text7.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text7.place(x=25,y=240)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=bgcolor, fg=fgcolor, font="15").place(x=10,y=27)
    b3 = Button(win3, text="Analyse", command = lambda:[clickanalyse(), showthis()],bg=fgcolor, fg=bgcolor, font="15").place(x=125,y=363)

def instructor(_filename_):
    docDir = './docs/'
    with open(docDir + _filename_, 'r') as theDoc:
        return theDoc.read()

def clickanalyse():
    for widget in win3.winfo_children():
        widget.destroy()

def showthis():
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=475, y=1)
    instructions = Text(win3, width="24",bg=bgcolor, fg=fgcolor, font="4",wrap = WORD, highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=255,y=2)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    label8 = Label(win3, text="Valid Query", bg=bgcolor, fg=fgcolor, font="6").place(x=10, y=70)
    text8 = Entry(win3, width="35",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text8.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text8.place(x=10,y=100)
    b8 = Button(win3, text="Next",command= lambda:[clickanalyse(), clicknext()], bg=fgcolor, fg=bgcolor, font="15").place(x=130,y=360)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=bgcolor, fg=fgcolor, font="15").place(x=20,y=20)

def clicknext():
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=460, y=1)
    label6 = Label(win3, text="Element", bg=bgcolor, fg=fgcolor, font="10")
    label6.place(x=20, y=10)
    instructions = scrolledtext.ScrolledText(win3, width="24",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1)
    instructions.config(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=240,y=2)
    instructions.insert(tk.END, instructor('S_PG2.md'))
    cbox = ttk.Combobox(win3, values=["XPATH", "CUSTOM"], state="readonly")
    cbox.place(x=20, y=40)    
    cbox.bind("<<ComboboxSelected>>", callbackFunc)
    global selection
    if cbox.get() == 'XPATH':        
        selection = cbox.get()
    if cbox.get() == 'CUSTOM':
        selection = cbox.get()
    
def callbackFunc(event):
    label11 = Label(win3, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6")
    text11 = Entry(win3, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1)
    text11.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    label9 = Label(win3, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6")
    text9 = Entry(win3, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text9.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
   
    label10 = Label(win3, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6")
    text10 = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text10.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
  
    b6 = Button(win3, text="Test",command = test, bg=fgcolor, fg=bgcolor, font="15")

    label7 = Label(win3, text="Xpath",bg=bgcolor, fg=fgcolor, font="6")
    text7 = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text7.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
  
    b7 = Button(win3, text="Test", command=test, bg=fgcolor, fg=bgcolor, font="15")



    selection = event.widget.get()
    if selection == 'CUSTOM': 
        label7.destroy()
        text7.destroy()
        b7.destroy()

        text11.place(x=20,y=90)
        label11.place(x=20,y=70)
        label9.place(x=50,y=130)
        text9.place(x=20,y=150)
        label10.place(x=20,y=180)
        text10.place(x=20,y=210)
        b6.place(x=150,y=335)
  
    elif selection == 'XPATH':
        label7.place(x=20,y=80)
        text7.place(x=20,y=100)
        b7.place(x=150,y=335)

        text11.destroy()
        label11.destroy()
        label9.destroy()
        text9.destroy()
        label10.destroy()
        text10.destroy()
        b6.destroy()

    else: print(None)    
  
    selection = ttk.Combobox(win3, width = 30)

def test():
    for widget in win3.winfo_children():
        widget.destroy()
    win3.title('info display')

root = Tk()                         # main screen window
root.title('Main window')
root.geometry("250x290+300+130")
root.resizable(width=False, height=False)
root.configure(bg=bgcolor)
root.overrideredirect(True)
b2 = Button(root, text ="+ Add website", command = lambda:[addsite(), closeroot()], bg=fgcolor, fg=bgcolor, height="1").place(x=120,y=253)
#b2['font'] = font.Font(size=6)
exitbutton = Button(root, text="X", command=root.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=230, y=6)
label1 = Label(root, text= "Term to be searched is:", bg=bgcolor, fg=fgcolor, font="4").place(x=30,y=20)
user_query = tk.StringVar(root, clipcopy())
text = Entry(root, width="30", fg=fgcolor, bg=bgcolor, textvariable = user_query, highlightthickness=1)
text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
text.place(x=30,y=50)

print(listdir('./profiles'))
profilelist = tk.Listbox(root, fg=fgcolor, bg=bgcolor, highlightthickness=1, width="30")
profilelist.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
profilelist.insert("end", *listdir('./profiles'))
profilelist.bind('<<ListboxSelect>>', getElement)
profilelist.place(x=30,y=80) 

mainloop()
