from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk

black = "#000000"
yellow = "#F8FC07"
white = "FFFFFF"

root = Tk()                         # main screen window
root.title('Main window')
root.geometry("600x500")
root.resizable(width=False, height=False)
root.configure(bg=black)

def closeroot():
    root.destroy()

def openwin2():    
    win2 = Tk()                     # search karne pe khulne wali window
    win2.title('info display(window 1)')
    win2.geometry("600x500")
    win2.resizable(width=False, height=False)
    win2.configure(bg=black)

    label2 = Label(win2, text="here the info will be displayed", bg=black, fg=yellow).pack()
    b3 = Button(win2, text = "Exit", command = win2.quit, bg=yellow, fg=black, font="15").place(x=500,y=680)

label1 = Label(root, text= "TERM TO BE SEARCHED IS:", bg=black, fg=yellow, font="12").pack()
text = Entry(root, width="30").place(x=200,y=50)

b1 = Button(root, text ="search", bg=yellow, command = lambda:[openwin2(), closeroot()], fg=black, font="10").place(x=255,y=100)

def addsite(): 
    global win3
    win3 = Tk()                         # add website karne pe khulne wali window
    win3.title('Link Analyzer(window 2)')
    win3.geometry("500x400")
    win3.configure(bg=black)
    win3.resizable(width=False, height=False)
    label4 = Label(win3, text="URL Sample 1", bg=black, fg=yellow, font="12").place(x=50,y=70)
    text4 = Entry(win3, width="40").place(x=50,y=90)
    text5 = Entry(win3, width="40").place(x=50,y=120)
    label5 = Label(win3, text="URL Sample 2", bg=black, fg=yellow, font="12").place(x=50,y=150)
    text6 = Entry(win3, width="40").place(x=50,y=170)
    text7 = Entry(win3, width="40").place(x=50,y=200)
    instructions = Label(win3,text="INSTRUCTIONS",bg=black, fg=yellow, font="15").place(x=350,y=10)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=black, fg=yellow, font="15").place(x=20,y=20)
    b3 = Button(win3, text="Analyse", command = lambda:[clickanalyse(), showthis()],bg=yellow, fg=black, font="15").place(x=230,y=360)
   
def clickanalyse():
    for widget in win3.winfo_children():
        widget.destroy()

def showthis():
    label8 = Label(win3, text="Valid Query", bg=black, fg=yellow, font="15").place(x=100, y=100)
    text8 = Entry(win3, width="30").place(x=100,y=150)
    b8 = Button(win3, text="Next",command= lambda:[clickanalyse(), clicknext()], bg=yellow, fg=black, font="15").place(x=230,y=360)
    instructions = Label(win3,text="INSTRUCTIONS",bg=black, fg=yellow, font="15").place(x=350,y=10)
    linkanalyse = Label(win3,text="LINK ANALYZER",bg=black, fg=yellow, font="15").place(x=20,y=20)

selection= ""
def clicknext():
    instructions = Label(win3,text="INSTRUCTIONS",bg=black, fg=yellow, font="25").place(x=350,y=10)
    label6 = Label(win3, text="Element", bg=black, fg=yellow, font="30")
    label6.place(x=60, y=50)
    b4 = Button(win3, text="Test", bg=yellow, fg=black, font="15").place(x=200,y=300)
    
    global selection
    cbox = ttk.Combobox(win3, values=["XPATH", "CUSTOM"], state="readonly")    
    cbox.place(x=60, y=100)
    # cbox.current(0) 
    if cbox.get() == 'XPATH':
        selection = cbox.get()
    if cbox.get() == 'CUSTOM':
        selection = cbox.get()
    cbox.bind("<<ComboboxSelected>>", clicknext)
    tk.Button(win3, text="Print C", command=printvalue, bg=black, fg=yellow, font="15").place(x=230,y=360)

def printvalue():
     print(selection)

# def ifcustom():
#     for widget in win3.winfo_children():
#         widget.destroy() 
#     label11 = Label(win3, text="Tag Name",bg=black, fg=yellow, font="30").place(x=100,y=300)
#     text11 = Entry(win3, width="70").place(x=100,y=350)
#     label9 = Label(win3, text="Attribute Name",bg=black, fg=yellow, font="30").place(x=100,y=400)
#     text9 = Entry(win3, width="70").place(x=100,y=450)
#     label10 = Label(win3, text="Attribute Value",bg=black, fg=yellow, font="30").place(x=100,y=500)
#     text10 = Entry(win3, width="70").place(x=100,y=550)

# def ifxpath():
#     for widget in win3.winfo_children():
#         widget.destroy() 
#     label7 = Label(win3, text="Xpath",bg=black, fg=yellow, font="30").place(x=100,y=200)
#     text7 = Entry(win3, width="70").place(x=100,y=250)    

#     label4 = Label(nx, text="URL Sample 1", bg=black, fg=yellow, font="12", visible='no').place(x=50,y=70)
#     text4 = Entry(nx, width="40", visible='no').place(x=50,y=90)
#     text5 = Entry(nx, width="40", visible='no').place(x=50,y=120)
#     label5 = Label(nx, text="URL Sample 2", bg=black, fg=yellow, font="12", visible='no').place(x=50,y=150)
#     text6 = Entry(nx, width="40", visible='no').place(x=50,y=170)
#     text7 = Entry(nx, width="40", visible='no').place(x=50,y=200) 

    
b2 = Button(root, text ="+ Add website", command = lambda:[addsite(), closeroot()], bg=yellow, fg=black, font="18").place(x=450,y=440)

 
    # win3 = Tk()              
    # win3.title('window 3')
    # win3.geometry("1000x1000")
    # win3.configure(bg=black)

    
#    profileGen.xpathGen()



mainloop()
