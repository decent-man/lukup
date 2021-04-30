from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
from clip import clipcopy
from os import listdir
from master import infoScraper

bgcolor = "#000000" #black
fgcolor = "#F8FC07" #yellow

root = Tk()                         # main screen window
root.title('Main window')
root.geometry("400x400+300+130")
root.resizable(width=False, height=False)
root.configure(bg=bgcolor)
root.overrideredirect(True)
b1 = Button(root, text ="Search", bg=fgcolor, command = lambda:[openwin2(), closeroot()], fg=bgcolor, font="10").place(x=30,y=80)
b2 = Button(root, text ="+ Add website", command = lambda:[addsite(), closeroot()], bg=fgcolor, fg=bgcolor, font="10").place(x=275,y=355)
exitbutton = Button(root, text="x", command=root.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=375, y=1)
label1 = Label(root, text= "Term to be searched is:", bg=bgcolor, fg=fgcolor, font="12").place(x=30,y=20)
user_query = tk.StringVar(root, clipcopy())
text = Entry(root, width="30", fg=fgcolor, bg=bgcolor, textvariable = user_query, highlightthickness=1)
text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
text.place(x=30,y=50)

print(listdir('./profiles'))
profilelist = tk.Listbox(root, fg=fgcolor, bg=bgcolor, highlightthickness=1)
profilelist.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
profilelist.insert("end", *listdir('./profiles'))

def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  print(value)
profilelist.bind('<<ListboxSelect>>', getElement)
profilelist.place(x=30,y=150) 

def closeroot():
    root.destroy()

def openwin2():
    win2 = Tk()                     # search karne pe khulne wali window
    win2.geometry("600x500+300+130")
    win2.resizable(width=False, height=False)
    win2.configure(bg=bgcolor) 
    win2.overrideredirect(True)  
    thecontent = infoScraper('./profiles/Wikipedia', clipcopy()) 
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
    instruct1 = """                  INSTRUCTIONS
1. Search for anything gibberish on the target website -example **ASPERO0** or **DA3MON**
2. Copy the URL of the website into the first sample box.
3. Repeat Steps 1 & 2 for the second sample box but with a different gibberish search term.
4. Now search for something relevant on the website and only provide the search term.
5. lukup will open the webpage in a browser with the inspector in element selection mode.
6. If the opened website matches the expected website proceed to the **Next** step.
7. If not some manual intervention is required. """
    instructions.place(x=255, y=2)
    instructions.insert(tk.END, instruct1)
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

def clickanalyse():
    for widget in win3.winfo_children():
        widget.destroy()

def showthis():
    exitbutton = Button(win3, text="x", command=win3.quit, bg=fgcolor, fg=bgcolor, width="2").place(x=475, y=1)
    instructions = Text(win3, width="24",bg=bgcolor, fg=fgcolor, font="4",wrap = WORD, highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instruct1 = """                  INSTRUCTIONS
1. Search for anything gibberish on the target website -example **ASPERO0** or **DA3MON**
2. Copy the URL of the website into the first sample box.
3. Repeat Steps 1 & 2 for the second sample box but with a different gibberish search term.
4. Now search for something relevant on the website and only provide the search term.
5. lukup will open the webpage in a browser with the inspector in element selection mode.
6. If the opened website matches the expected website proceed to the **Next** step.
7. If not some manual intervention is required. """
    instructions.place(x=255,y=2)
    instructions.insert(tk.END, instruct1)
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
    scroll = Scrollbar(win3)
    scroll.pack(side=RIGHT, fill=Y)
    instructions = Text(win3, width="24",bg=bgcolor, fg=fgcolor, font="4",wrap = WORD, yscrollcommand = scroll.set, highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instruct2 = """           INSTRUCTIONS
This section involves capturing accurate html tag information for lukup to scrape correctly.
1. In the opened webpage, select and click on the element that contains the information you want to fetch.
2. Upon clicking the element's tag will be highlighted.
3. Beyond this there are two ways you can proceed:
    1. **The XPATH method**:
        This method is the "easier" option, but as all things easy it comes with a higher chance of inaccuracy.
        - Right click on the `id` attribute of the tag and select Copy XPATH from within the menu/submenu.
        - Paste this information in the Xpath field.
        - Press the **Test** button.
        - Lukup will generate appropriate profiles for the website and launch the testing sample window.
        - If the information in the sample window is as expected then Save the configuration and exit the setup.
    2. **The Manual Method**(Recommended):
        This is the preferred method of grabbing element data. This method has the highest accuracy.
        Once the required tag is highlighted in the inspector:
        - Input the **tag** name into the **Tag** field. Usually these would be `div`,`span`,etc at the beginning right after `<`.
        - Choose any **attribute name** in the **tag** and input this into the **Attribute Name** field. Ideally the best choice is the `id`, but in some websites there maybe more than one elements with the same id - this will cause problems. You can however enter any attribute like `class`,`itemtype`,etc just make sure it is unique.
        - Enter the **attribute's value** in the **Attribute Value** field. This would be the value of the attribute you chose written after `=` within quotation marks.
        - E.g For a tag like `<div id="mw-content-text" class="main-results">`
            - `div` will go in the **Tag** field.
            - `id` OR `class` will go in **Attribute Name** field.
            - `mw-content-text` OR `main-results`(depending on above choice) will go in **Attribute Value** field. 
        - Press the **Test** button.
        - Lukup will generate appropriate profiles for the website and launch the testing sample window.
        - If the information in the sample window is as expected then Save the configuration and exit the setup."""
    scroll.config(command=instructions.yview, activebackground=bgcolor)
    instructions.place(x=240,y=2)
    instructions.insert(tk.END, instruct2)
    cbox = ttk.Combobox(win3, values=["XPATH", "CUSTOM"], state="readonly")
    cbox.place(x=20, y=40)    
    cbox.bind("<<ComboboxSelected>>", callbackFunc)
    global selection
    if cbox.get() == 'XPATH':        
        selection = cbox.get()
    if cbox.get() == 'CUSTOM':
        selection = cbox.get()
    
def callbackFunc(event):
    selection = event.widget.get()
    if selection == 'CUSTOM':   
        ifcustom()  
    if selection == 'XPATH':
        ifxpath()
    selection = ttk.Combobox(win3, width = 30)

def test():
    for widget in win3.winfo_children():
        widget.destroy()
    win3.title('info display')

  

def ifcustom():
    # for widget in win3.winfo_children():
    #     widget.destroy()
    label11 = Label(win3, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=70)
    text11 = Entry(win3, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1)
    text11.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text11.place(x=20,y=90)
    label9 = Label(win3, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6").place(x=50,y=130)
    text9 = Entry(win3, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text9.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text9.place(x=20,y=150)
    label10 = Label(win3, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=180)
    text10 = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text10.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text10.place(x=20,y=210)
    b6 = Button(win3, text="Test",command = test, bg=fgcolor, fg=bgcolor, font="15").place(x=150,y=335)

def ifxpath():
    # for widget in win3.winfo_children():
    #     widget.destroy()
    label7 = Label(win3, text="Xpath",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=80)
    text7 = Entry(win3, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    text7.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    text7.place(x=20,y=100)
    b7 = Button(win3, text="Test", command=test, bg=fgcolor, fg=bgcolor, font="15").place(x=150,y=335)

mainloop()
