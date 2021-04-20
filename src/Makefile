INTERP=python
T_FILE=another.py

S_FILE=setup.py
S_ARG1="https://wiki.archlinux.org/index.php?search=ASPERO0+GETARO1&title=Special%3ASearch&go=Go"
S_ARG2=ASPERO0
S_ARG3="https://wiki.archlinux.org/index.php?search=DA3MON+B01&title=Special%3ASearch&go=Go"
S_ARG4=DA3MON
S_ARG5=AMDGPU PRO

MASTER=master.py
M_FILE=profiles/ArchWiki
M_ARG2="AMDGPU PRO"


setup: setup.py
	./$(S_FILE) $(S_ARG1) $(S_ARG2) $(S_ARG3) $(S_ARG4) $(S_ARG5)
test:
	$(INTERP) $(T_FILE) $(S_ARG1) $(S_ARG2) $(S_ARG3) $(S_ARG4) $(S_ARG5) 
master:
	./$(MASTER) $(M_FILE) $(M_ARG2)
cl:
	rm -rf geckodriver.log __pycache__
