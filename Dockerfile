# Pull base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /activity-app


RUN apk --update --upgrade add bash gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf

# make psycopg2-binary install on alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1 #Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 #Prevents Python from buffering stdout and stderr

# Install dependencies
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt && \
    rm -rf /root/.cache && \
    sed -i "s/EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'/EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'/" activity/settings/local-sample.py && \
    chmod 777 /activity-app/.docker/start_app.sh
