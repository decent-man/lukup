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
fgcolor = "#FFFFFF" #yellow

class wInit:
    def __init__(self,geom,colors):
        self = Tk()
        self.geometry(geom)
        self.resizable(width=False, height=False)
        self.configure(bg=colors)
        self.overrideredirect(True)
    def kill(self):
        self.destroy()

def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  profile = './profiles/' + value
  print(profile)
  openwin2(search_term_text.get(), profile)

def openwin2(_query_, _profile_):
    root.destroy()
    win2 = Tk()                     # search karne pe khulne wali window
    win2.geometry("600x500+300+130")
    win2.resizable(width=False, height=False)
    win2.configure(bg=bgcolor) 
    win2.overrideredirect(True)     
    thecontent = infoScraper(_profile_, _query_) 
    titlelabel = Label(win2, text= thecontent[0], fg=bgcolor, bg=fgcolor).place(x=10,y=10)
    information = scrolledtext.ScrolledText(win2, width="62",bg=bgcolor, fg=fgcolor, font="4", wrap=WORD, highlightthickness=1)
    information.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    info = thecontent[1]   
    information.place(x=10, y=40)
    information.insert(tk.END, info)
    exitbutton = Button(win2, text="x", command=win2.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=564, y=6)

def addsite():
    global win3
    win3 = Tk()                         # add website karne pe khulne wali window
    win3.title('Link Analyzer(window 2)')
    win3.geometry("500x400+300+130")
    win3.configure(bg=bgcolor)
    win3.overrideredirect(True)
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=479, y=6)
    win3.resizable(width=False, height=False)
    instructions = scrolledtext.ScrolledText(win3, width="24",bg=bgcolor, fg=fgcolor, font="1",wrap = WORD, highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228, y=30)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    url1label = Label(win3, text="URL Sample 1", bg=bgcolor, fg=fgcolor).place(x=25,y=70)
    url1text = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url1text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url1text.place(x=25,y=90)
    url1_text = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url1_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url1_text.place(x=25,y=120)
    url2label = Label(win3, text="URL Sample 2", bg=bgcolor, fg=fgcolor).place(x=25,y=160)
    url2text = Entry(win3, width="30",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url2text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url2text.place(x=25,y=180)
    url2_text = Entry(win3, width="30",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url2_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url2_text.place(x=25,y=210)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=bgcolor, fg=fgcolor, font="15").place(x=10,y=30)
    analyzbtn = Button(win3, text="Analyse", command = lambda:[clickanalyse(), showthis()],bg=fgcolor, fg=bgcolor).place(x=125,y=363)

def instructor(_filename_):
    docDir = './docs/'
    with open(docDir + _filename_, 'r') as theDoc:
        return theDoc.read()

def clickanalyse():
    for widget in win3.winfo_children():
        widget.destroy()

def showthis():
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=479, y=6)
    instructions = scrolledtext.ScrolledText(win3, width="24",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1)
    instructions.config(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228,y=30)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    validentrylabel = Label(win3, text="Valid Query", bg=bgcolor, fg=fgcolor).place(x=10, y=70)
    validentrytext = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    validentrytext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    validentrytext.place(x=10,y=90)
    nxtbtn = Button(win3, text="Next",command= lambda:[clickanalyse(), clicknext()], bg=fgcolor, fg=bgcolor).place(x=130,y=360)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=bgcolor, fg=fgcolor, font="15").place(x=20,y=30)

def clicknext():
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=479, y=6)
    elementlabel = Label(win3, text="Element", bg=bgcolor, fg=fgcolor, font="10")
    elementlabel.place(x=20, y=35)
    instructions = scrolledtext.ScrolledText(win3, width="24",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1)
    instructions.config(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228,y=35)
    instructions.insert(tk.END, instructor('S_PG2.md'))
    cbox = ttk.Combobox(win3, values=["XPATH", "CUSTOM"], state="readonly")
    cbox.place(x=20, y=60)    
    cbox.bind("<<ComboboxSelected>>", callbackFunc)
    global selection
    if cbox.get() == 'XPATH':        
        selection = cbox.get()
    if cbox.get() == 'CUSTOM':
        selection = cbox.get()
    
def callbackFunc(event):
    tagnamelabel = Label(win3, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6")
    tagnametext = Entry(win3, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1)
    tagnametext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    attributenamelabel = Label(win3, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6")
    attributenametext = Entry(win3, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1)
    attributenametext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
   
    attribute_val_label = Label(win3, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6")
    attribute_val_text = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    attribute_val_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
  
    testbtn = Button(win3, text="Test",command = test, bg=fgcolor, fg=bgcolor, font="15")

    xpathlabel = Label(win3, text="Xpath",bg=bgcolor, fg=fgcolor, font="6")
    xpathtext = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    xpathtext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
  
    testbtn = Button(win3, text="Test", command=test, bg=fgcolor, fg=bgcolor, font="15")

    
    selection = event.widget.get()
    if selection == 'CUSTOM': 
        xpathlabel.destroy()
        xpathtext.destroy()
        testbtn.destroy()
        
        tagnamelabel.place(x=20,y=110)
        tagnametext.place(x=20,y=130)
        attributenamelabel.place(x=20,y=170)
        attributenametext.place(x=20,y=190)
        attribute_val_label.place(x=20,y=230)
        attribute_val_text.place(x=20,y=250)
        testbtn.place(x=150,y=335)
  
    elif selection == 'XPATH':
        xpathlabel.place(x=20,y=110)
        xpathtext.place(x=20,y=130)
        testbtn.place(x=150,y=335)

        tagnametext.destroy()
        tagnamelabel.destroy()
        attributenamelabel.destroy()
        attributenametext.destroy()
        attribute_val_label.destroy()
        attribute_val_text.destroy()
        testbtn.destroy()

    else: print(None)    
  
    selection = ttk.Combobox(win3, width = 30)

def test():
    for widget in win3.winfo_children():
        widget.destroy()
    win3.title('info display')

root = Tk()                         # main screen window
root.title('Main window')
root.geometry("250x290+500+170")
root.resizable(width=False, height=False)
root.configure(bg=bgcolor)
root.overrideredirect(True)
addsitebtn = Button(root, text ="+ Add website", command = lambda:[addsite(), closeroot()], bg=fgcolor, fg=bgcolor, height="1").place(x=120,y=253)
exitbutton = Button(root, text="x", command=root.quit, bg=bgcolor, fg=fgcolor, width="1").place(x=210, y=6)
search_term_label = Label(root, text= "Term to be searched is:", bg=bgcolor, fg=fgcolor, font="4").place(x=30,y=20)
user_query = tk.StringVar(root, clipcopy())
search_term_text = Entry(root, width="30", fg=fgcolor, bg=bgcolor, textvariable = user_query, highlightthickness=1)
search_term_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
search_term_text.place(x=30,y=50)
# print(listdir('./profiles'))
profilelist = tk.Listbox(root, fg=fgcolor, bg=bgcolor, highlightthickness=1, width="30")
profilelist.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
profilelist.insert("end", *listdir('./profiles'))
profilelist.bind('<<ListboxSelect>>', getElement)
profilelist.place(x=30,y=80) 

mainloop()
