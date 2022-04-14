
# We Use an official Python runtime as a parent image
FROM python:3.10.4-bullseye
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /usr/src/django_test/
RUN mkdir /usr/src/django_test/library
# Set the working directory to 
WORKDIR /usr/src/django_test/library
# Copy the current directory contents into the container at 
ADD . /usr/src/django_test/library
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
