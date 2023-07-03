#!/bin/bash

awslocal lambda create-function \
    --function-name fn_teste \
    --runtime python3.9 \
    --role any \
    --handler Src.handler.handler \
    --zip-file fileb://src.zip