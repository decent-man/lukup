from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

black = "#000000"
yellow = "#F8FC07"
white = "FFFFFF"

root = Tk()                         # main screen window
root.title('Main window')
root.geometry("1000x1000")
# root.state('zoomed')
root.configure(bg=black)

def closeroot():
    root.destroy()

def openwin2():    
    win2 = Tk()                     # search karne pe khulne wali window
    win2.title('info display(window 1)')
    win2.geometry("1000x1000")
    win2.configure(bg=black)

    label2 = Label(win2, text="here the info will be displayed", bg=black, fg=yellow).pack()
    b3 = Button(win2, text = "Exit", command = win2.quit, bg=yellow, fg=black, font="15").place(x=500,y=680)

label1 = Label(root, text= "TERM TO BE SEARCHED IS:", bg=black, fg=yellow, font="15").pack()
text = Entry(root, width="30").place(x=420,y=50)

b1 = Button(root, text ="search", bg=yellow, command = lambda:[openwin2(), closeroot()], fg=black, font="10").place(x=465,y=100)


def addsite():  
    nx = Tk()                         # add website karne pe khulne wali window
    nx.title('Link Analyzer(window 2)')
    nx.geometry("1000x1000")
    nx.configure(bg=black)
    label4 = Label(nx, text="URL Sample 1", bg=black, fg=yellow, font="18").place(x=50,y=70)
    text4 = Entry(nx, width="60").place(x=50,y=90)
    label5 = Label(nx, text="URL Sample 2", bg=black, fg=yellow, font="18").place(x=50,y=120)
    text5 = Entry(nx, width="60").place(x=50,y=140)
    instructions = Label(nx,text="INSTRUCTIONS",bg=black, fg=yellow, font="25").place(x=750,y=10)
    linkanalyse = Label(nx,text="LINK ANALYZER",bg=black, fg=yellow, font="40").place(x=20,y=20)
    b3 = Button(nx, text="Next", command = lambda:[clicknext(), closenx()], bg=yellow, fg=black, font="15").place(x=500,y=680) #lambda func not working properly

def closenx():
    nx.destroy()

b2 = Button(root, text ="+ Add website", command = lambda:[addsite(), closeroot()], bg=yellow, fg=black, font="18").place(x=850,y=680) #lambda func working properly


def closewin3():
    win3.destroy()

def clicknext():  
    win3 = Tk()                         # next click karne pe khulne wali window fsdfsadaasf
    win3.title('window 3')
    win3.geometry("1000x1000")
    # win3.configure(bg=black)
    instructions = Label(win3,text="INSTRUCTIONS",bg=black, fg=yellow, font="25").place(x=750,y=10)
    data = ["XPATH", "CUSTOM"]
    label6 = Label(win3, text="Element", bg=black, fg=yellow, font="30")
    label6.place(x=100, y=50)
    b4 = Button(win3, text="Test", bg=yellow, fg=black, font="15").place(x=500,y=680)
    combo = Combobox(win3, values=data, width="50")
    combo.place(x=100, y=80)
    combo.current(0) 
   
# def selection():
    
#     val = combo.get()
#     messagebox.showinfo("selection", val)

    # label7 = Label(win3, text="Xpath",bg=black, fg=yellow, font="30").place(x=100,y=200)
    # text7 = Entry(win3, width="70").place(x=100,y=250)
    # label8 = Label(win3, text="Tag Name",bg=black, fg=yellow, font="30").place(x=100,y=300)
    # text8 = Entry(win3, width="70").place(x=100,y=350)
    # label9 = Label(win3, text="Attribute Name",bg=black, fg=yellow, font="30").place(x=100,y=400)
    # text9 = Entry(win3, width="70").place(x=100,y=450)
    # label10 = Label(win3, text="Attribute Value",bg=black, fg=yellow, font="30").place(x=100,y=500)
    # text10 = Entry(win3, width="70").place(x=100,y=550)



# def clicktest():
#     win4 = Tk()                         # test click karne pe khulne wali window
#     win4.title('window 4')
#     win4.geometry("1000x1000")
#     win4.configure(bg=black)
#     instructions = Label(win4,text="INSTRUCTIONS",bg=black, fg=yellow, font="25").place(x=750,y=10)    

mainloop()
