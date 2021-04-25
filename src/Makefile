INTERP=python

# Temporary test files
T_FILE=another.py

# setup.py
S_FILE=setup.py
S_ARG1="https://wiki.archlinux.org/index.php?search=ASPERO0+GETARO1&title=Special%3ASearch&go=Go"
S_ARG2=ASPERO0
S_ARG3="https://wiki.archlinux.org/index.php?search=DA3MON+B01&title=Special%3ASearch&go=Go"
S_ARG4=DA3MON
S_ARG5=AMDGPU PRO

# master.py
MASTER=master.py
M_FILE=profiles/ArchWiki
M_ARG2="AMDGPU PRO"

# clip.py
CLIP_FILE=clip.py

# index.py
GUI_FILE=index.py

setup: $(S_FILE)
	$(INTERP) $(S_FILE) $(S_ARG1) $(S_ARG2) $(S_ARG3) $(S_ARG4) $(S_ARG5)

test:
	$(INTERP) $(T_FILE) $(S_ARG1) $(S_ARG2) $(S_ARG3) $(S_ARG4) $(S_ARG5) 

master: $(MASTER)
	$(INTERP) $(MASTER) $(M_FILE) $(M_ARG2)

gui: $(GUI_FILE)
	$(INTERP) $(GUI_FILE)

clip: $(CLIP_FILE)
	$(INTERP) $(CLIP_FILE)

#Cleanup scripts
cl: clip.py docs/* index.py Makefile master.py profiles/* requirements rolback/* setup.py test.py 
	rm -rf geckodriver.log __pycache__
wincl:
	RD /S __pycache__
	DEL /F /A geckodriver.log
