SHELL := /bin/bash

install: 
	( \
	   python3 -m venv venv; \
       source venv/bin/activate; \
       pip install ply; \
    )

clean:
	( \
       rm -rf venv; \
    )

run: 
	( \
       source venv/bin/activate; \
       python main.py; \
    )
	