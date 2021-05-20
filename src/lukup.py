#!/usr/bin/python
from tkinter import Button,Entry,Frame,Label,Tk,Listbox,StringVar,END,NORMAL,X,Y,WORD,BOTH,DISABLED
from tkinter.ttk import Combobox
from os import listdir,remove
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
import markdown
from tkhtmlview import HTMLScrolledText

from pyperclip import paste as clipFetch

# Local Modules
from master import infoScraper
import setup as st

# ENV's
BGCOLOR = "#000000" #black
FGCOLOR = "#FFFFFF" #yellow
SELDRIVER = '/home/rakshit/Downloads/geckodriver'
BROWSER = 'FI'
ENTER='<Return>'
SDOCS= './docs/'

class wInit(Tk):
    def __init__(self,geom,colors,browObj=None):
        Tk.__init__(self)
        self.geometry(geom)
        self.resizable(width=False, height=False)
        self.configure(bg=colors)
        self.overrideredirect(False)
        if browObj is None:
            self.bind('<Escape>', lambda kPress:[self.quit()])
        else:
            self.bind('<Escape>', lambda kPress:[self.quit(),browObj.quit()])
    def kill(self):
        self.destroy()

class wExit(Button):
    def __init__(self,currentWin,winX: int,winY: int):
        placeX = winX - 30
        placeY = 6
        fntAwes = Font(family='Font Awesome 5 Free Solid',size=12)
        Button.__init__(self,currentWin, text="x", command=currentWin.quit, bg=BGCOLOR, fg=FGCOLOR, width="1",padx=5,pady=2,font=fntAwes)
        # Button.__init__(self,currentWin, text="", command=currentWin.quit, bg=BGCOLOR, fg=FGCOLOR, width="1",padx=5,pady=2,font=fntAwes)
        self.place(x=placeX, y=placeY)

class hbxInstruct(HTMLScrolledText,markdown.Markdown):
    def __init__(self,windoe,file,winX:int,winY:int):
        HTMLScrolledText.__init__(self,windoe, width="37", html=hbxInstruct.hinstFetch(file))
        placeX = winX - 272
        placeY = winY - 363
        self.place(x=placeX,y=placeY)
    def hinstFetch(_filename_):
        with open(SDOCS + _filename_, 'r') as theDoc:
            return markdown.markdown(theDoc.read())

class bxInstruct(ScrolledText):
    def __init__(self,windoe,file,winX:int,winY:int):
        ScrolledText.__init__(self,windoe, width="37",bg=BGCOLOR, fg=FGCOLOR, font="4", wrap=WORD, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
        self.insert(END,bxInstruct.instFetch('S_PG1.md'))
        placeX = winX - 272
        placeY = winY - 363
        self.place(x=placeX,y=placeY)
    def instFetch(_filename_):
        with open(SDOCS + _filename_, 'r') as theDoc:
            return markdown.markdown(theDoc.read())


def cleanChildren(_win_):
    for widget in _win_.winfo_children():
        widget.destroy()

def instructor(_filename_:str):
    print(SDOCS + _filename_)
    with open(SDOCS + _filename_, 'r') as theDoc:
        return markdown.markdown(theDoc.read())

def getElement(event,query,homWin):
    profile = './profiles/' + str(event.widget.get(event.widget.curselection()[0]))
    print(profile)
    print(query)
    cleanChildren(homWin)
    homWin.kill()
    openResult(query.get(), profile)

def openResult(_query_, _profile_):
    WinResult = wInit("600x345+800+230",BGCOLOR)
    thecontent = infoScraper(_profile_, _query_)
    Label(WinResult, text= thecontent[0], fg=BGCOLOR, bg=FGCOLOR).pack(fill=X,expand=True)
    information = ScrolledText(WinResult,bg=BGCOLOR, fg=FGCOLOR, font="4", wrap=WORD, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    info = thecontent[1]
    information.pack(fill=X,expand=True)
    information.insert(END, info)
    wExit(WinResult,600,345)

def addsite(roots):
    roots.destroy()
    WinSetup = wInit("500x400+300+130",BGCOLOR)
    wExit(WinSetup,500,400)
    hbxInstruct(WinSetup,"S_PG1.md",500,400)
    Label(WinSetup, text="URL Sample 1", bg=BGCOLOR, fg=FGCOLOR).place(x=25,y=70)
    url1Link = Entry(WinSetup, width="30", bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    url1Link.place(x=25,y=90)
    url1Query = Entry(WinSetup, width="30", bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    url1Query.place(x=25,y=120)
    Label(WinSetup, text="URL Sample 2", bg=BGCOLOR, fg=FGCOLOR).place(x=25,y=160)
    url2Link = Entry(WinSetup, width="30",  bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    url2Link.place(x=25,y=180)
    url2Query = Entry(WinSetup, width="30",  bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    url2Query.place(x=25,y=210)
    Label(WinSetup,text="LINK ANALYZER",bg=BGCOLOR, fg=FGCOLOR, font="15").place(x=10,y=30)
    Button(WinSetup, text="Analyse", command = lambda:[clickAnalyse(WinSetup,url1Link.get(),url1Query.get(),url2Link.get(),url2Query.get())],bg=FGCOLOR, fg=BGCOLOR).place(x=125,y=363)

def clickAnalyse(window,u1,q1,u2,q2):
    datStatic = st.linkAnalyzer(u1,q1,u2,q2)
    assert (datStatic != None), "ERROR::Match_Failed :- Static URL's Mismatched"
    print(datStatic)
    cleanChildren(window)
    wExit(window,500,400)
    Label(window,text="Link Analyzer",bg=BGCOLOR, fg=FGCOLOR, font="15").place(x=20,y=30)
    hbxInstruct(window,"S_PG1.md",500,400)
    Label(window, text="Valid Query", bg=BGCOLOR, fg=FGCOLOR).place(x=10, y=70)
    valQuery = Entry(window, width="30", bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    valQuery.place(x=10,y=90)
    valQuery.bind(ENTER,lambda kPress:[clickNext(window,datStatic,valQuery.get())])
    Button(window, text="Next",command=lambda:[clickNext(window,datStatic,valQuery.get())], bg=FGCOLOR, fg=BGCOLOR).place(x=130,y=360)


def clickNext(winElem,_static_,_queryStr_):
    urlTo = st.genURL(_static_,_queryStr_)
    print(urlTo)
    cleanChildren(winElem)
    myBrows = st.browserInit(urlTo,SELDRIVER,BROWSER)
    wExit(winElem,500,400)
    elementlabel = Label(winElem, text="Element Data", bg=BGCOLOR, fg=FGCOLOR, font="10")
    elementlabel.place(x=20, y=35)
    hbxInstruct(winElem,"S_PG2.md",500,400)
    tgNL = Label(winElem, text="Tag Name",bg=BGCOLOR, fg=FGCOLOR, font="6").place(x=20,y=110)
    tgN = Entry(winElem, width="30",bg = BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    tgN.place(x=20,y=130)
    atNL = Label(winElem, text="Attribute Name",bg=BGCOLOR, fg=FGCOLOR, font="6").place(x=20,y=170)
    atN = Entry(winElem, width="30",bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    atN.place(x=20,y=190)
    atvL = Label(winElem, text="Attribute Value",bg=BGCOLOR, fg=FGCOLOR, font="6").place(x=20,y=230)
    atV = Entry(winElem, width="30",bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    atV.place(x=20,y=250)
    atV.bind(ENTER,lambda kPress:[runTest(winElem,_static_,_queryStr_,tgN.get(),atN.get(),atV.get(),myBrows)])
    testbtn = Button(winElem, text="Test", command=lambda:[runTest(winElem,_static_,_queryStr_,tgN.get(),atN.get(),atV.get(),myBrows)], bg=FGCOLOR, fg=BGCOLOR, font="10",state=NORMAL)
    testbtn.place(x=150,y=335)

def runTest(elemWin,_static_,_queries_,_tag_,_atN_,_atV_,brows):
    tesWin = wInit("600x380+300+130",BGCOLOR,brows)
    st.profileGen(_static_,"t35t",_tag_,_atN_,_atV_)
    infoTuple = infoScraper("t35t",_queries_)
    contentBox = ScrolledText(tesWin, width=40 , height=20 , bg=BGCOLOR, fg=FGCOLOR, font="4", highlightthickness=1,highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    contentBox.pack(fill=X,expand=True)
    contentBox.insert(END,infoTuple[1])
    Button(tesWin, text =" <- ", command=tesWin.destroy, bg=FGCOLOR, fg=BGCOLOR, height="1",padx=4,pady=2).place(x=10,y=15)
    Label(tesWin,text="Save Configuration as:", fg=FGCOLOR,bg=BGCOLOR,font="6").place(x=25,y=320)
    siteNames = Entry(tesWin, width="50", bg=BGCOLOR, fg=FGCOLOR, highlightthickness=1, highlightbackground=FGCOLOR, highlightcolor=FGCOLOR)
    siteNames.place(x=25,y=345)
    cnfSave = Button(tesWin, text ="Confirm & Save", command=lambda:[makeProfile(_static_,_queries_,_tag_,_atN_,_atV_,siteNames.get()),tesWin.quit(),elemWin.quit(),home(),brows.quit()], bg=FGCOLOR, fg=BGCOLOR, height="1")
    cnfSave.place(x=460,y=340)

def makeProfile(_static_,_queries_,_tag_,_atN_,_atV_,filename):
    st.profileGen(_static_,str("./profiles/" + filename),_tag_,_atN_,_atV_)
    remove("t35t")

def home():
    root = wInit("250x290+600+180",BGCOLOR)
    addsitebtn = Button(root, text ="+ Add website", command=lambda:[addsite(root)], bg=FGCOLOR, fg=BGCOLOR, height="1").place(x=120,y=253)
    wExit(root,250,290)
    Label(root, text= "Term to be searched is:", bg=BGCOLOR, fg=FGCOLOR, font="4").place(x=30,y=20)
    uQuery = StringVar()
    uQuery.set(clipFetch())
    qBox = Entry(root, width="30", textvariable=uQuery, fg=FGCOLOR, bg=BGCOLOR, highlightthickness=1, highlightbackground=FGCOLOR, highlightcolor=FGCOLOR)
    qBox.place(x=30,y=50)
    profilelist = Listbox(root, fg=FGCOLOR, bg=BGCOLOR, highlightthickness=1, width="30",highlightbackground = FGCOLOR, highlightcolor= FGCOLOR)
    profilelist.insert("end", *listdir('./profiles'))
    profilelist.bind('<<ListboxSelect>>', lambda ev,sQry=uQuery,homeWind=root:[getElement(ev,sQry,homeWind)])
    profilelist.place(x=30,y=80)
    root.mainloop()
