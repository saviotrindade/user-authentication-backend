#!/bin/bash

python3 -m pip install -r requirements.txt

mkdir app
mkdir app/api
mkdir app/core
mkdir app/models
mkdir app/schemas
mkdir app/services

touch .env
touch app.py