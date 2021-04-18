INTERP=python
T_FILE=another.py
FILE=setup.py
ARG1="https://wiki.archlinux.org/index.php?search=ASPERO0+GETARO1&title=Special%3ASearch&go=Go"
ARG2=ASPERO0
ARG3="https://wiki.archlinux.org/index.php?search=DA3MON+B01&title=Special%3ASearch&go=Go"
ARG4=DA3MON
ARG5=AMDGPU PRO

setup: setup.py
	./$(FILE) $(ARG1) $(ARG2) $(ARG3) $(ARG4) $(ARG5)
test:
	$(INTERP) $(T_FILE) $(ARG1) $(ARG2) $(ARG3) $(ARG4) $(ARG5) 
cl:
	rm -rf geckodriver.log __pycache__
