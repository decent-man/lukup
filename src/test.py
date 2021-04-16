from master import dhe_scraper # <= import like this
import sys                     # <= needed to read arguments
print(dhe_scraper(sys.argv[1]))
#                      /\
#                      ||
#           It takes file name as input

# Run this file as:-  python test.py profiles/<<PROFILE_FILE>>.json <<Search_Keyword_Here>>
#                                             /\                            /\
#                                             ||                            ||
#                                   Input the json file as the       Input the search term as the 
#                                   first argument.                  second argument.
#                                   All json files are stored
#                                   in "profiles" directory.
