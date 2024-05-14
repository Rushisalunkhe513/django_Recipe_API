# lets get base image
FROM python:3.9-alpine3.13

# labler (who created and maintianing this Dockerfile)
LABEL maintainer="rushisalunkhe513"

# ENV var (PYTHONUNBUFFERED is used for sending output of python code directly to terminal without being buffered)
ENV PYTHONUNBUFFERED 1

# copy required files and app code
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
EXPOSE 8000

# run command for updating pip package manager and install dependencies.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 
# --no-cache-dir means no cache will be stored whih may cause some conflicts and every time dependencie will be instaled freshely.