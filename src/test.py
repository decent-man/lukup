from master import infoScraper # <= import like this
import sys                     # <= needed to read arguments
print(infoScraper(sys.argv[1])) # <= This is only a test print. Only to show that the output of the function is the partial html file.
#                      /\            To seperate out the text you might need to refer to the commented lines 32 & 33 in master.py - "for content in mainContent: print(content.text)" 
#                      ||
#           It takes file name as input

# Run this file as:-  python test.py profiles/<<PROFILE_FILE>>.json <<Search_Keyword_Here>>
#                                             /\                            /\
#                                             ||                            ||
#                                   Input the json file as the       Input the search term as the 
#                                   first argument.                  second argument.
#                                   All json files are stored
#                                   in "profiles" directory.
