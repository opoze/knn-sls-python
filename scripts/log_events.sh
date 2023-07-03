#!/bin/bash

awslocal logs get-log-events --log-group-name /aws/lambda/predict-function --log-stream-name log-stream --output text

