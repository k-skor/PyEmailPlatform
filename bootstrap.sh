#!/bin/bash

export FLASK_APP=email_platform
source venv/bin/activate
flask run -h 0.0.0.0
