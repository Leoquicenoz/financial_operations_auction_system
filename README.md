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

Open the browser and go to:

```python
http://localhost:8000/docs
```

You will see the following interface

<img src="https://github.com/user-attachments/assets/b31d87e6-104a-449e-a643-5de6d87ad3c6" width="800">

<details>

<summary>Register users</summary>

To register users you need to assign: `username`, `password` and `role` (the only options available in this field are *Operator*/*Investor*).

You can do it using directly the end point with the “*Try it out*” option and entering the values directly, after that you press the “*Execute*” button.

<img src="https://github.com/user-attachments/assets/df6ddbdf-7961-4a75-a1ee-9bd6618da54b" width="800">

<img src="https://github.com/user-attachments/assets/e4673e92-171c-4fc0-83a4-451a56483334" width="800">

Or using a tool such as Postman

<img src="https://github.com/user-attachments/assets/9eec74dc-7b70-426c-b672-85c2441946a1" width="800">

</details>

<details>

<summary>Token generation</summary>

A token must be generated to authorize registered users to create operations or place bids, depending on the user's role.

<img src="https://github.com/user-attachments/assets/4f886b07-817e-48bb-ae8a-4088be84ea75" width="800">

<img src="https://github.com/user-attachments/assets/32cfb72d-0fa8-4176-a2e9-70134e9ff372" width="800">

</details>

<details>

<summary>Login using token</summary>

To log in and be able to use the features that require authorization, you must click on the lock button at the top right of the *Operations* and *Bids* endpoints.
In the “`client_secret`” field you must enter the token generated for the user you want to log in (bear in mind that the token lasts 30 minutes, after this time a new one must be generated).

<img src="https://github.com/user-attachments/assets/c50d817e-82eb-44b7-8b1e-60dee99cf8cf" width="400">

<img src="https://github.com/user-attachments/assets/ac9d3c1d-3f8c-4ee1-943a-6fc3b9bf8ea4" width="400">

</details>

<details>

<summary>Create operations and Bids</summary>

Once the user is logged in can proceed to create operations or place bids. If the user is an Operator can create operations and if is an Investor can place bids on existing operations.

<img src="https://github.com/user-attachments/assets/854b39a1-59a0-424d-a71b-22e69b7776ab" width="800">

<img src="https://github.com/user-attachments/assets/492c6cf6-1d12-4e8d-bb13-649f82f0260b" width="800">

</details>

<details>

<summary>Requests</summary>

Any user can make these three requests:

1. **List active operations**: The result of this query will deliver a list of the operations that are open at that moment, each operation will have 5 data corresponding to: `operation id`, `amount`, `annual interest` and `operator id`.

<img src="https://github.com/user-attachments/assets/7186e648-e460-48ea-adaf-b62d3c20d5ce" width="800">

2. **Show specific operation**: The `operation id` is used to filter and show only the required operation.

<img src="https://github.com/user-attachments/assets/ec3d1b54-a79c-44e8-be23-726661985f88" width="800">

3. **Show bids by operation**: The `operation id` is used to filter and display the bids that have been placed on this specific operation.

<img src="https://github.com/user-attachments/assets/4b472fbe-7a6a-4c5a-834e-dfe7780d5455" width="800">

</details>

## Testing






Author: Leonardo Quiceno| 2024
 
