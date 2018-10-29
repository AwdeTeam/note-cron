run: env
	flask run

env:
	export FLASK_APP=./notecron.py

deenv:
	env -u FLASK_APP

.PHONY: run, env, deenv
