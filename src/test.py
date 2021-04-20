from master import infoScraper # <= import like this
#                          And search query as second input
#                               ||
#                               \/  
print(infoScraper(file_path,search_query)) # <= This is only a test print. Only to show that the output of the function is the partial html file.
#                      /\            To seperate out the text you might need to refer to the commented lines 32 & 33 in master.py - "for content in mainContent: print(content.text)" 
#                      ||
#           It takes file name as first input

# Run this file as:-  python test.py profiles/<<PROFILE_FILE>>.json <<Search_Keyword_Here>>
#                                             /\                            /\
#                                             ||                            ||
#                                   Input the json file as the       Input the search term as the 
#                                   first argument.                  second argument.
#                                   All json files are stored
#                                   in "profiles" directory.
#
#
#     It returns the html segment as output for now. I will make it so it returns only text and title.
