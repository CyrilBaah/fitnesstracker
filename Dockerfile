FROM python:3.8-slim-buster

# Python environment setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set working directory
ENV PROJECT=/home/app

RUN mkdir -p ${PROJECT}
RUN mkdir -p ${PROJECT}/static
WORKDIR ${PROJECT}

# Packages required for setting up WSGI
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev python3-dev

# Copy and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt ${PROJECT}/requirements.txt
RUN pip install -r ${PROJECT}/requirements.txt

# Copy project to working directory
COPY . ${PROJECT}

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "/home/app/entrypoint.sh"]

