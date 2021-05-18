import tkinter as tk
from tkinter import ttk
from clip import clipcopy
from os import listdir
from master import infoScraper
import tkinter.font as font
import tkinter.scrolledtext as scrolledtext
import setup as st

#Default ENV's
bgcolor = "#000000" #black
fgcolor = "#FFFFFF" #yellow
SELDRIVER = '/home/rakshit/Downloads/geckodriver'
BROWSER = 'FI'

class wInit(tk.Tk):
    def __init__(self,geom,colors):
        tk.Tk.__init__(self)
        self.geometry(geom)
        self.resizable(width=False, height=False)
        self.configure(bg=colors)
        self.overrideredirect(False)
    def kill(self):
        self.destroy()

def cleanChildren(_win_):
    for widget in _win_.winfo_children():
        widget.destroy()


def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  profile = './profiles/' + value
  print(profile)
  openResult(search_term_text.get(), profile)

def openResult(_query_, _profile_):
    root.destroy()
    WinResult = wInit("600x500+300+130",bgcolor)
    thecontent = infoScraper(_profile_, _query_) 
    titlelabel = tk.Label(WinResult, text= thecontent[0], fg=bgcolor, bg=fgcolor).place(x=10,y=10)
    information = scrolledtext.ScrolledText(WinResult, width="62",bg=bgcolor, fg=fgcolor, font="4", wrap=WORD, highlightthickness=1)
    information.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    info = thecontent[1]   
    information.place(x=10, y=40)
    information.insert(tk.END, info)
    exitbutton = tk.Button(WinResult, text="x", command=WinResult.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=564, y=6)

def instructor(_filename_):
    docDir = './docs/'
    with open(docDir + _filename_, 'r') as theDoc:
        return theDoc.read()

def addsite(roots):
    roots.destroy()
    WinSetup = wInit("500x400+300+130",bgcolor)
    exitbutton = tk.Button(WinSetup, text="x", command=WinSetup.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=449, y=6)
    instructions = scrolledtext.ScrolledText(WinSetup, width="37",bg=bgcolor, fg=fgcolor, font="1", highlightthickness=1)
    instructions.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228, y=37)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    url1label = tk.Label(WinSetup, text="URL Sample 1", bg=bgcolor, fg=fgcolor).place(x=25,y=70)
    url1Link = tk.Entry(WinSetup, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url1Link.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url1Link.place(x=25,y=90)
    url1Query = tk.Entry(WinSetup, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url1Query.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url1Query.place(x=25,y=120)
    url2label = tk.Label(WinSetup, text="URL Sample 2", bg=bgcolor, fg=fgcolor).place(x=25,y=160)
    url2Link = tk.Entry(WinSetup, width="30",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url2Link.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url2Link.place(x=25,y=180)
    url2Query = tk.Entry(WinSetup, width="30",  bg=bgcolor, fg=fgcolor, highlightthickness=1)
    url2Query.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    url2Query.place(x=25,y=210)
    linkanalyse = tk.Label(WinSetup,text="LINK ANALYZER",bg=bgcolor, fg=fgcolor, font="15").place(x=10,y=30)
    analyzbtn = tk.Button(WinSetup, text="Analyse", command = lambda:[clickAnalyse(WinSetup,url1Link.get(),url1Query.get(),url2Link.get(),url2Query.get())],bg=fgcolor, fg=bgcolor).place(x=125,y=363)

def clickAnalyse(window,u1,q1,u2,q2):
    datStatic = st.linkAnalyzer(u1,q1,u2,q2)
    assert (datStatic != None), "ERROR::Match_Failed :- Static URL's Mismatched"
    print(datStatic)
    cleanChildren(window)
    exitbutton = tk.Button(window, text="x", command=window.quit, bg=fgcolor, fg=bgcolor, width="1").place(x=449, y=6)
    instructions = scrolledtext.ScrolledText(window, width="37",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1)
    instructions.config(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228,y=37)
    instructions.insert(tk.END, instructor('S_PG1.md'))
    validentrylabel = tk.Label(window, text="Valid Query", bg=bgcolor, fg=fgcolor).place(x=10, y=70)
    validentrytext = tk.Entry(window, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1)
    validentrytext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    validentrytext.place(x=10,y=90)
    nxtbtn = tk.Button(window, text="Next",command=lambda:[clickNext(window,datStatic,validentrytext.get())], bg=fgcolor, fg=bgcolor).place(x=130,y=360)
    linkanalyse = tk.Label(window,text="Link Analyzer",bg=bgcolor, fg=fgcolor, font="15").place(x=20,y=30)

def clickNext(winElem,_static_,_queryStr_):
    urlTo = st.genURL(_static_,_queryStr_)
    print(urlTo)
    cleanChildren(winElem)
    myBrows = st.browserInit(urlTo,SELDRIVER,BROWSER)
    exitbutton = tk.Button(winElem, text="x", command=lambda:[winElem.quit(),myBrows.quit()], bg=fgcolor, fg=bgcolor, width="1").place(x=449, y=6)
    elementlabel = tk.Label(winElem, text="Element Data", bg=bgcolor, fg=fgcolor, font="10")
    elementlabel.place(x=20, y=35)
    instructions = scrolledtext.ScrolledText(winElem, width="37",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1)
    instructions.config(highlightbackground = fgcolor, highlightcolor= fgcolor)
    instructions.place(x=228,y=37)
    instructions.insert(tk.END, instructor('S_PG2.md'))
    tk.Label(winElem, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=110)
    tgN = tk.Entry(winElem, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    tgN.place(x=20,y=130)
    tk.Label(winElem, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=170)
    atN = tk.Entry(winElem, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    atN.place(x=20,y=190)
    tk.Label(winElem, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=230)
    atV = tk.Entry(winElem, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    atV.place(x=20,y=250)
    testbtn = tk.Button(winElem, text="Test", command=lambda:[runTest(winElem,_static_,_queryStr_,tgN.get(),atN.get(),atV.get(),)], bg=fgcolor, fg=bgcolor, font="10",state=tk.NORMAL)
    testbtn.place(x=150,y=335)
    # cbox = ttk.Combobox(winElem, values=["XPATH", "CUSTOM"], state="readonly")
    # cbox.place(x=20, y=60)    
    # cbox.bind("<<ComboboxSelected>>",callbackFunc)
    
# def callbackFunc(event):
    # windObj = event.widget.master
    # #manual widgets
    # cFrame = ttk.Frame(windObj,height=20,width=15,padding=(50,50,50,50))
    # cFrame.grid(row=2,column=6)
    # # tagnamelabel = tk.Label(cFrame, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6").
    # # tagnametext = tk.Entry(cFrame, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    # # # tagnametext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    # tk.Label(cFrame, text="Tag Name",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=110)
    # tk.Entry(cFrame, width="30",bg = bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor).place(x=20,y=120)

    # # attributenamelabel = tk.Label(cFrame, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6")
    # # attributenametext = tk.Entry(cFrame, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    # # attributenametext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    # tk.Label(cFrame, text="Attribute Name",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=130)
    # tk.Entry(cFrame, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor).place(x=20,y=140)
   
    # # attribute_val_label = tk.Label(cFrame, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6")
    # # attribute_val_text = tk.Entry(cFrame, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    # # attribute_val_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    # tk.Label(cFrame, text="Attribute Value",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=150)
    # tk.Entry(cFrame, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor).place(x=20,y=160)
  
    # #xpath widget
    # # xFrame = ttk.Frame(windObj,x=100,y=25,bg="#FFFF00")
    # xFrame = ttk.Frame(windObj,height=20,width=15,padding=(50,50,50,50))
    # xFrame.grid(row=2,column=6)
    # # xpathlabel = tk.Label(xFrame, text="Xpath",bg=bgcolor, fg=fgcolor, font="6")
    # # xpathtext = tk.Entry(xFrame, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    # # xpathtext.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
    # tk.Label(xFrame, text="Xpath",bg=bgcolor, fg=fgcolor, font="6").place(x=20,y=110)
    # tk.Entry(xFrame, width="30", bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor).place(x=20,y=120)
  
    # testbtn = tk.Button(windObj, text="Test", command=runTest, bg=fgcolor, fg=bgcolor, font="10",state=tk.DISABLED)
    # testbtn.place(x=150,y=335)
    
    # selection = event.widget.get()
    # if selection == 'CUSTOM': 
        # # xpathlabel.destroy()
        # # print(None)
        # # xpathtext.destroy()
        
        # # tagnamelabel.place(x=20,y=110)
        # # tagnametext.place(x=20,y=130)
        # # attributenamelabel.place(x=20,y=170)
        # # attributenametext.place(x=20,y=190)
        # # attribute_val_label.place(x=20,y=230)
        # # attribute_val_text.place(x=20,y=250)
        # # testbtn.config(state=tk.NORMAL)
        # # cFrame.pack()
        # xFrame.place(x=70,y=15)
  
    # elif selection == 'XPATH':
        # print(None)
        # # xpathlabel.place(x=20,y=110)
        # # xpathtext.place(x=20,y=130)
        # # # testbtn.place(x=150,y=335)

        # # tagnametext.destroy()
        # # tagnamelabel.destroy()
        # # attributenamelabel.destroy()
        # # attributenametext.destroy()
        # # attribute_val_label.destroy()
        # # attribute_val_text.destroy()
        # # testbtn.config(state=tk.NORMAL)
        # # xFrame.place(x=50,y=15)
        # xFrame.place(x=50,y=15)

    # else: print("\n=\n")    
  
    # # selection = ttk.Combobox(windObj, width = 30)

def runTest(elemWin,_static_,_queries_,_tag_,_atN_,_atV_):
    tesWin = wInit("600x500+300+130",bgcolor)
    st.profileGen(_static_,"test",_tag_,_atN_,_atV_)
    infoTuple = infoScraper("test",_queries_)
    goBack = tk.Button(tesWin, text =" < ", command=tesWin.quit, bg=fgcolor, fg=bgcolor, height="1")
    goBack.place(x=20,y=25)
    siteNames = tk.Entry(tesWin, width="30",bg=bgcolor, fg=fgcolor, highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    siteNames.place(x=25,y=455)
    contentBox = scrolledtext.ScrolledText(tesWin, width="69",bg=bgcolor, fg=fgcolor, font="4", highlightthickness=1,highlightbackground = fgcolor, highlightcolor= fgcolor)
    contentBox.place(x=10,y=40)
    contentBox.insert(tk.END,infoTuple[1])
    cnfSave = tk.Button(tesWin, text ="Confirm & Save", command=lambda:[makeProfile(_static_,_queries_,_tag_,_atN_,_atV_,siteNames.get()),tesWin.quit()], bg=fgcolor, fg=bgcolor, height="1")
    cnfSave.place(x=390,y=455)

def makeProfile(_static_,_queries_,_tag_,_atN_,_atV_,filename):
    st.profileGen(_static_,str("./profiles/" + filename),_tag_,_atN_,_atV_)

root = wInit("250x290+500+170",bgcolor)
addsitebtn = tk.Button(root, text ="+ Add website", command=lambda:[addsite(root)], bg=fgcolor, fg=bgcolor, height="1").place(x=120,y=253)
exitbutton = tk.Button(root, text="x", command=root.quit, bg=bgcolor, fg=fgcolor, width="1").place(x=210, y=6)
search_term_label = tk.Label(root, text= "Term to be searched is:", bg=bgcolor, fg=fgcolor, font="4").place(x=30,y=20)
user_query = tk.StringVar(root, clipcopy())
search_term_text = tk.Entry(root, width="30", fg=fgcolor, bg=bgcolor, textvariable = user_query, highlightthickness=1)
search_term_text.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
search_term_text.place(x=30,y=50)
# print(listdir('./profiles'))
profilelist = tk.Listbox(root, fg=fgcolor, bg=bgcolor, highlightthickness=1, width="30")
profilelist.configure(highlightbackground = fgcolor, highlightcolor= fgcolor)
profilelist.insert("end", *listdir('./profiles'))
profilelist.bind('<<ListboxSelect>>', getElement)
profilelist.place(x=30,y=80) 

root.mainloop()
