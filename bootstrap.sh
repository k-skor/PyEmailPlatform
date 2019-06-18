#!/bin/bash

export FLASK_APP=./email-platform/index.py
source venv/bin/activate
flask run -h 0.0.0.0
