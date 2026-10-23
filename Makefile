install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py 

all: install lint test format
