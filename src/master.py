#!/usr/bin/python
import sys
import lxml
import requests
from bs4 import BeautifulSoup as BS

def infoScraper(_profile_file_,_query_):
    LINE_CHAR = "="
    
    with open(_profile_file_) as config:
        import json
        cfg   = json.load(config)
        U_A = cfg['AGENT']
        REF = cfg['REFERER']
        U_SEP = cfg['SEP'] 
        # URL   = cfg['URL'] + U_SEP.join(str(word) for word in sys.argv[2:])
        URL   = cfg['URL'] + _query_.replace(" ",U_SEP)
        TAG   = cfg['TAG_TYPE']
        ATTRID = cfg['ATTR_NAM']
        ATTRVAL = cfg['ATTR_VAL']
    
    with requests.Session() as RQ:
        RQ.headers = { "User-Agent" : U_A , "Referer": REF }
        html = BS(RQ.get(URL,stream=True).text, 'lxml')
        title = html.find('title')
        mainContent = html.find(TAG , attrs={ATTRID:ATTRVAL})
        # contentMain = []
        # for content in mainContent:
            # contentMain.append(content.text)
        
    return (title.text,mainContent.text)

# print(infoScraper(sys.argv[1],sys.argv[2]))
    # print("\n=====================================\n")
    # print("Seperator: " + U_SEP + "\nProcessed Link:" + URL)
    # print(URL)
    # print(SESSION_HEADER)
    # print("\n=====================================\n")
###########################################################3
        # print(html.prettify())
        # print(LINE_CHAR*len(URL))
        # print("\t" + title.text + "\n" + URL)
        # print(LINE_CHAR*len(URL))
        # for content in mainContent:
            # print(content.text)
        # print("<EOF>")
        # print("  Done Closing requests.")
