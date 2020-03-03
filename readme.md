# STA 9760 Project - Analyzing Millions of NYC Parking Violations

## Project Introduction

In this project, I will be performing data analysis on the Open Parking and Camera Violations data, which is obtained from the NYC Open Data.

## Part 1 - Python Scripting

In the part 1 of the project, I will be setting up a python command line interface that can connect to the OPCV API. First I created a Dockerfile that contains instructions on how to build the images.

```
# This is my Dockerfile
FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
COPY . /app

RUN pip install -r requirements.txt
```

The requirements.txt file contains the dependency that I need in this project. In this case, there is only one dependency which is the Pypl's sodapy module. This module allows me to the Socrata API, which I use to get the data. <br />
<br />
Then I use the following command to build the Docker image.

```
docker build -t bigdata1:1.0 .
```

Then I can use the following command to run my code.

```
docker run -e APP_KEY={app_key} -t bigdata1:1.0 python main.py --page_size=2 --num_pages=3
```

- APP_KEY: The app_key that is used in the script to get the data using the API

- bigdata1: The name of the docker image.

- --page_size: This argument is **required**. Number of records to request from each API call.

- --num_pages: This argument is **optional**. Number of times to make a API call. If this argument is not given, the script will keep requesting data until all the data has been exhausted.

- --output: This argument is **optional**. If not given, the script will print the results to stdout. If given, the script will write the data to a file.

To use my Docker image and run my code on EC2, first you have to login to Docker from EC2 and pull my image.

```
sudo docker pull henrychon/bigdata1:1.1
```

Run the following command on EC2 to run the code

```
sudo docker run -e APP_KEY={app_key} -t henrychon/bigdata1:1.1 python main.py --page_size=2 --num_pages=3 --output.txt
```

<br />

## Part 2 - Loading into ElasticSearch

Coming Soon

<br />

## Part 3 - Visualizing and ANalysis on Kibana

Coming Soon
