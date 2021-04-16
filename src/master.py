#!/usr/bin/python3.8
import sys
import lxml
import json
import requests
from bs4 import BeautifulSoup as BS

def dhe_scraper(PROFILE):
    LINE_CHAR = "="
    
    with open(PROFILE) as config:
        cfg   = json.load(config)
        U_SEP = cfg['SEP'] 
        URL   = cfg['URL'] + U_SEP.join(str(word) for word in sys.argv[2:])
        TAG   = cfg['TAG_TYPE']
        ATTRID = cfg['ATTR_NAM']
        ATTRVAL = cfg['ATTR_VAL']
        U_A = cfg['AGENT']
        REF = cfg['REFERER']
    
    with requests.Session() as RQ:
        RQ.headers = { "User-Agent" : U_A , "Referer": REF }
        html = BS(RQ.get(URL).text, 'lxml')
        title = html.find('title')
        mainContent = html.find_all(TAG , attrs={ATTRID:ATTRVAL})
        return mainContent
        # print(html.prettify())
        # print(LINE_CHAR*len(URL))
        # print("\t" + title.text + "\n" + URL)
        # print(LINE_CHAR*len(URL))
        # for content in mainContent:
            # print(content.text)
        # print("<EOF>")
        # print("  Done Closing requests.")

print(dhe_scraper(sys.argv[1]))
    # @dataclass
    # class O_Model:
         #DATA CLASS GENERATOR CODE
    
    # print("\n=====================================\n")
    # print("Seperator: " + U_SEP + "\nProcessed Link:" + URL)
    # print(URL)
    # print(SESSION_HEADER)
    # print("\n=====================================\n")
