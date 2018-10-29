run:
	export FLASK_APP=./notecron.py
	flask run
	env -u FLASK_APP

.PHONY: run
