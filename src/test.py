#
#  Instructions for importing and using master.py
#
from master import infoScraper # <= import like this OR just use "import master"
#                          And search query as second input
#                               ||
#                               \/  
print(infoScraper(file_path,search_query)) # <= This is only a test print. Only to show that the output of the function is the partial html file.
#                      /\            To seperate out the text you might need to refer to the commented lines 32 & 33 in master.py - "for content in mainContent: print(content.text)" 
#                      ||
#           It takes file name as first input

#
#     It returns the (title,html_code) , a tuple, as output for now. I will make it so it returns only text instead of the raw html. But for now it is how it is.


#
#   Instructions for importing and using setup.py
#
import setup

print(linkAnalyzer(<PROVIDE_ARGUMENTS_HERE>)) # <= The linkAnalyzer - will be used in page 1 of setup to generate static url
print(genURL(<PROVIDE_ARGUMENTS_HERE>))       # <= The URL maker - will be used to generate correct url from query to open in browser
print(browserInit(<PROVIDE_ARGUMENTS_HERE>))  # <= The browser launcher - it will open up the browser->inspector->selection_mode for the user. Will be used for Page 2 of setup
print(profileGen.xpathGen(<PROVIDE_ARGUMENTS_HERE>)) OR print(profileGen.manualGen(<PROVIDE_ARGUMENTS_HERE>)) # <= The Profile Generator - will be used in Page 2 for generating the website's json
