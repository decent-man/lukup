#!/usr/bin/python
import sys
import pyautogui
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from dataclasses import dataclass, asdict

#=====THE_FUNDAMENTALS=====
def linkAnalyzer(GIBRL,GIBQUERY,GIB2RL,GIB2QUERY): ## <= Compares url's and queries and strips out the static part of the url.
    #
    def Gen_STATIC(rawlink,query):
       query_pos = rawlink.lower().find(query.lower())
       return str(rawlink[0:query_pos]) #(Cuts the string to the point until the searched query word is found.)
    #
    staticParsed = (Gen_STATIC(GIBRL,GIBQUERY),Gen_STATIC(GIB2RL,GIB2QUERY)) #Both query's parsed and stored into a tuple.
    if staticParsed[0] == staticParsed[1]:
        return str(staticParsed[1])         ## <= Returns the string containing the static part of the url. Will be used by the next function.
    else:
        return None


def genURL(static,query,seperator='+'): ## <= Generates a web acceptable url. Will be used to feed link to open in the browser.
   return static + query.replace(" ",seperator) #(combines the static_URL with the valid search query and replaces spaces with '+')


def browserInit(_url_,driverloc,_browserName_): ## <= Opens the browser->Inspector->SelectionMode. Returns the webdriver object for use later.
   supBrows = ('CH','FI','ED','IN','SA','OP') ## <= Use these values for 3rd parameter(_browserName_).
   # assert (_browserName_ in supBrows), "ERROR::UNKNOWN_BROWSER_QUERY!"
   if _browserName_.upper() in supBrows: 
       if _browserName_.upper() == supBrows[0]:
           browser = webdriver.Chrome(executable_path=driverloc) #Chrome browser code
       elif _browserName_.upper() == supBrows[1]:
           browser = webdriver.Firefox(executable_path=driverloc) #Firefox browser code
       elif _browserName_.upper() == supBrows[2]:
           browser = webdriver.Edge(executable_path=driverloc) #Edge browser code
       elif _browserName_.upper() == supBrows[3]:
           browser = webdriver.Ie(executable_path=driverloc) #Internet Explorer browser code
       elif _browserName_.upper() == supBrows[4]:
           browser = webdriver.Opera(executable_path=driverloc) #Opera browser code
       elif _browserName_.upper() == supBrows[5]:
           browser = webdriver.Safari(executable_path=driverloc) #Safari browser code
   else:
       print("ERROR::BROWSER_NOT_FOUND::Unsupported Browser Error!")
       return None
   browser.get(_url_)
   # pyautogui.press('f12')
   pyautogui.hotkey('ctrl','shift','i') #more universal than f12.
   pyautogui.hotkey('ctrl','shift','c')
   return browser

#=====GENERATORS===========
def Gen_JSON(profileobj):
    return json.dumps(asdict(profileobj),sort_keys=True,indent=0)

def Write_JSON(jsonobj,siteName):
    open(siteName,'w').write(jsonobj)
#==========x===============

def profileGen(_static_,_filename_,_tagid_,_attrid_,_attrval_):                ## <= Used to generate the 'profile.json'. Not usable directly. Subfunctions 'xpathGen' OR 'manualGen' to be called accordingly.
    @dataclass
    class PROFILE:
        AGENT: str
        REFERER: str
        URL: str
        SEP: str
        TAG_TYPE: str
        ATTR_NAM: str
        ATTR_VAL: str

    STOCK_UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9139690441 t38550 ath9b965f92 altpub cvcv=2'
    STOCK_REFERER = 'https://duckduckgo.com?q=wiki'
    STOCK_SEP='+'
    VANILLA_ATTR='id'
    #
    # def xpathGen(_static_,_filename_,_driver_,_xpath_): ## <= Generates profile from xpath. Does not return anything.
        # ##
        # def XP_to_Manual(_tagname_,_attrib_,_attribval_):
            # # import re
            # # TAG_LIST = [_tagname_]                
            # # TAG_LIST += re.findall('@[a-z-]+=',xpath)
            # # TAG_LIST += re.findall('\"[a-z-]+\"',xpath)
            # # return [TAG_LIST[0],TAG_LIST[1][1:-1],TAG_LIST[2][1:-1]]
            # return [_tagname_,_attrib_,_attribval_]
        # ##
        # # manual_list = XP_to_Manual(_driver_.find_element(By.XPATH,_xpath_).tag_name,_xpath_)
        # mainTag = _driver_.find_element(By.XPATH,_xpath_)
        # manual_list = XP_to_Manual(mainTag.tag_name,VANILLA_ATTR,mainTag.get_attribute(VANILLA_ATTR))
        # Write_JSON(Gen_JSON(PROFILE(STOCK_UA,STOCK_REFERER,_static_,STOCK_SEP,manual_list[0],manual_list[1],manual_list[2])),_filename_)
    # #
    Write_JSON(Gen_JSON(PROFILE(STOCK_UA,STOCK_REFERER,_static_,STOCK_SEP,_tagid_,_attrid_,_attrval_)),_filename_)
    # def manualGen(_static_,_filename_,_tagid_,_attrid_,_attrval_): ## <= Generates profile from manual entries. Does not return anything.
        # Write_JSON(Gen_JSON(PROFILE(STOCK_UA,STOCK_REFERER,_static_,STOCK_SEP,_tagid_,_attrid_,_attrval_)),_filename_)



