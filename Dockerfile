FROM python:3.7-alpine
LABEL maintainer="Michael Hixson"


#python does not buffer outputs, instead prints them directly
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -D create user to run apps only, does not have homedir ect. just to run processes
RUN adduser -D user

#switch to this user, otherwise the image will run this app as root. not good.
USER user