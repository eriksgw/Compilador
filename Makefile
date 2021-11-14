SHELL := /bin/bash

# PYTHON v3.8.10 
install: 
	( \
      sudo apt-get -y install python3-pip; \
      pip3 install ply; \
   )

clean:
	( \
      pip3 uninstall ply; \
   )

run: 
	( \
      python3 main.py $(file); \
   )