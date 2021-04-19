#!/usr/bin/python
import sys
import time
import pyautogui
import json
from dataclasses import dataclass, asdict
from selenium import webdriver
from selenium.webdriver.common.by import By

#=========VAR's============
FIRE_PATH='/home/rakshit/Downloads/geckodriver'
GIBRL=sys.argv[1]
GIBQUERY=sys.argv[2]
GIB2RL=sys.argv[3]
GIB2QUERY=sys.argv[4]

DEFAULT_SEP="+"

VALID_QUERY=sys.argv[5:]

DEFAULT_UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9139690441 t38550 ath9b965f92 altpub cvcv=2'
DEFAULT_REFERER = 'https://duckduckgo.com?q=wiki'
SAMPLE_XPATH = './/*[@id="content"]'
TAG=""
ATTRN=""
ATTRTY=""
SAMPLE_FILENAME="ArchWiki"
#==========================

#=====PROFILE_DATACLASS==========
@dataclass
class PROFILE:
    AGENT: str
    REFERER: str
    URL: str
    SEP: str
    TAG_TYPE: str
    ATTR_ID: str
    ATTR_VAL: str
#=========================

#=====CORE_FUNCTION========
def coreSetup():
   staticParsed = (Gen_STATIC(GIBRL,GIBQUERY),Gen_STATIC(GIB2RL,GIB2QUERY)) #Both query's parsed and stored into a tuple.

   if staticParsed[0] == staticParsed[1]:
       browser = webdriver.Firefox(executable_path=FIRE_PATH)
       browser.get(Gen_URL(staticParsed[1],VALID_QUERY))
       pyautogui.press('f12')
       pyautogui.hotkey('ctrl','shift','c')
       #CALL WINDOW TO FEED THE TAGS
       XPATH_MODE=True
       STATIC_URL=staticParsed[1]
       if XPATH_MODE is True:
           elem = browser.find_element(By.XPATH,'.//*[@id="content"]')
           manual_list = XP_to_Manual(elem.tag_name,SAMPLE_XPATH)
           Write_JSON(Gen_JSON(PROFILE(DEFAULT_UA,DEFAULT_REFERER,STATIC_URL,DEFAULT_SEP,manual_list[0],manual_list[1],manual_list[2])),SAMPLE_FILENAME)
       else:
           Write_JSON(Gen_JSON(PROFILE(DEFAULT_UA,DEFAULT_REFERER,STATIC_URL,DEFAULT_SEP,TAG_ID,ATTRIBUTE_ID,ATTRIBUTE_VALUE)),SAMPLE_FILENAME)
       # time.sleep(15)
       browser.quit()
       
   else:
      #PARSE_MISMATCH - do some extra hoops
      print("REGEX_FAILURE:PARSE:1")
#==========================

def linkAnalyzer(GIBRL,GIBQUERY,GIB2RL,GIB2QUERY):
   staticParsed = (Gen_STATIC(GIBRL,GIBQUERY),Gen_STATIC(GIB2RL,GIB2QUERY)) #Both query's parsed and stored into a tuple.
   if staticParsed[0] == staticParsed[1]:
       return staticParsed[1]
   else:
       return None

#=====GENERATORS===========
def Gen_STATIC(rawlink,query):
   query_pos = rawlink.lower().find(query.lower())
   return str(rawlink[0:query_pos]) # Cuts the string to the point until the searched query word is found.

def Gen_URL(static,query):
   return static + DEFAULT_SEP.join(str(word) for word in query) #combines the static_URL with the valid search query and replaces spaces with '+'

def Gen_JSON(profileobj):
    return json.dumps(asdict(profileobj),sort_keys=True,indent=0)

def Write_JSON(jsonobj,siteName):
    open(siteName,'w').write(jsonobj)

def XP_to_Manual(tagname,xpath):
    import re
    TAG_LIST = [tagname]                
    TAG_LIST += re.findall('@[a-z-]+=',xpath)
    TAG_LIST += re.findall('\"[a-z-]+\"',xpath)
    return [TAG_LIST[0],TAG_LIST[1][1:-1],TAG_LIST[2][1:-1]]
#==========================

coreSetup()
