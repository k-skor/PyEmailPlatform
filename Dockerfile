FROM python:3.6-alpine

RUN apk update
RUN python3 -m pip install --no-cache-dir virtualenv

WORKDIR /usr/src/app
COPY setup.py requirements.txt bootstrap.sh ./
COPY email_platform ./email_platform
RUN mkdir ./email_platform/db

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
RUN python -m email_platform.build_database

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
