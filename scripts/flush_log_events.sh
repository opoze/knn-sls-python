#!/bin/bash

awslocal logs delete-log-stream --log-group-name /aws/lambda/predict-function --log-stream-name log-stream
awslocal logs create-log-stream --log-group-name /aws/lambda/predict-function --log-stream-name log-stream

