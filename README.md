# Auction API

<img src="https://github.com/user-attachments/assets/be2a0e99-891c-46d0-8583-1641fc072df0" width="300">



## Overview
This is an API built with FastAPI, and allow users to create financial operations that can be financed by investors through an auction process. 

Only two types of users can be created (`Operators`/`Investors`), each user has different functionalities enabled and there are some that are common, below is a description of the functionalities and which users are enabled to use them:

1) Create financial operations. (Only operators)
2) Bid to finance an operation. (Only investors)
3) List active operations. (Any user)
4) View details of a operations. (Any user)
5) List bids for a specific operation. (Any user)

## Content
* [Overview](#Overview)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Usage](#Usage)
* [Testing](#Testing)

## Technologies

This project uses the following Python dependencies:
* uvicorn
* fastapi
* pydantic
* passlib
* python-jose
* pytz
* python-multipart
* pytest
* httpx
* python-dotenv

These are included in the requirements.txt file and will be installed automatically following the steps in the Setup section.

## Setup
To run locally

```python
# Within a local folder, Clone this repository

$git clone https://github.com/Leoquicenoz/financial_operations_auction_system.git

# And locate yourself in the root of the project (financial_operations_auction_system)
```
```python
# The project has the following file structure

├── README.md
├── app
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers
│         ├── bids.py
│         ├── operations.py
│         └── users.py
├── test
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_bids.py
│   ├── test_operations.py
│   └── test_users.py
├── .env
├── .env.example
├── .gitignore
├── auction_system.db
├── pictures
├── docker-compose.yml
├── Dockerfile
├── Makefile
└── requirements.txt
```
You must not have the `.env` file available, since the `SECRET_KEY` variable is stored in it, so you will need to create in the root of this project a file with the name `.env` and in it you must add the `SECRET_KEY` (this will be provided by the creator of the project privately).


This app uses Docker for created a deploy enviroment, you must have Docker installed and running.

Create and activate a virtual environment to install the dependencies included in `requirements.txt`

```python
$python -m venv venv
$source venv/bin/activate
```
Once the virtual environment and the `.env` file (with the appropriate `SECRET_KEY`) have been created, run the following command:

```python
$make run
```
You will get the following output: 

```python
docker-compose up --build
[+] Building 19.5s (10/10) FINISHED                                             
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 437B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.12.3           3.9s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [1/5] FROM docker.io/library/python:3.12.3@sha256:3966b81808d864099f8  0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 13.45MB                                       0.1s
 => CACHED [2/5] WORKDIR /app                                              0.0s
 => [3/5] COPY requirements.txt .                                          0.0s
 => [4/5] RUN pip install -r requirements.txt                             15.2s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     0.2s 
 => => exporting layers                                                    0.2s 
 => => writing image sha256:68dce6b198f66d627fed45903619823958b250be5b06c  0.0s 
 => => naming to docker.io/library/financial_operations_auction_system-fa  0.0s 
[+] Running 1/0                                                                 
 ⠿ Container financial_operations_auction_system-fastapi-app-1  Recreated  0.0s
Attaching to financial_operations_auction_system-fastapi-app-1
financial_operations_auction_system-fastapi-app-1  | INFO:     Will watch for changes in these directories: ['/app']
financial_operations_auction_system-fastapi-app-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
financial_operations_auction_system-fastapi-app-1  | INFO:     Started reloader process [1] using StatReload
financial_operations_auction_system-fastapi-app-1  | INFO:     Started server process [8]
financial_operations_auction_system-fastapi-app-1  | INFO:     Waiting for application startup.
financial_operations_auction_system-fastapi-app-1  | INFO:     Application startup complete.
```

This indicates that the app is ready for use!!!

## Usage

Open the browser and go to 

```python
http://localhost:8000/docs
```

You will see the following interface






## Testing





Author: Leonardo Quiceno| 2024
