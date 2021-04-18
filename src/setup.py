#!/usr/bin/python
import sys
import time
import pyautogui
from selenium import webdriver
# irrelevent modules - for now
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

FIRE_PATH='/home/rakshit/Downloads/geckodriver'
GIBRL=sys.argv[1]
GIBQUERY=sys.argv[2]
GIB2RL=sys.argv[3]
GIB2QUERY=sys.argv[4]

DEFAULT_SEP="+"

VALID_QUERY=sys.argv[5:]

DEFAULT_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9139690441 t38550 ath9b965f92 altpub cvcv=2",
DEFAULT_REFERER = "https://duckduckgo.com?q=wiki",
TAG = ""

def browInspector():
   ##Search for a GIBBERISH query user!
   gib1URL = generate_static(GIBRL,GIBQUERY) 
   ##Search for a GIBBERISH query again user!
   gib2URL = generate_static(GIB2RL,GIB2QUERY)
   print("\nGibberish1 URL:" + GIBRL + "\nGibberish Parsed:" + gib1URL + "\n\nGibberish2 URL:" + GIB2RL + "\nGibberish2 Parsed:" + gib2URL + "\n" )

   if gib2URL == gib1URL:
       browser = webdriver.Firefox(executable_path=FIRE_PATH)
       browser.get(generate_url(gib1URL,VALID_QUERY))
       # print(generate_url(gib1URL,VALID_QUERY))
       #ask if opened page matches the expected page.
       # browser.find_element_by_tag_name('body').send_keys(Keys.ALT + Keys.SHIFT + 'f') # this works for some reason - only strokes sent to the body work
       pyautogui.press('f12')
       pyautogui.hotkey('ctrl','shift','c')
       #CALL WINDOW TO FEED THE TAG
       time.sleep(15)
       browser.quit()

   else:
      #PARSE_MISMATCH - do some extra hoops
      print("REGEX_FAILURE:PARSE:1")


def generate_static(rawlink,query):
   query_pos = rawlink.lower().find(query.lower())
   return str(rawlink[0:query_pos]) # Cuts the string to the point until the searched query word is found.

def generate_url(static,query):
   return static + DEFAULT_SEP.join(str(word) for word in query) #combines the static_url with the valid search query and replaces spaces with '+'

browInspector()
