#!/bin/bash

awslocal lambda get-function --function-name master-degree-serverless-dev-predict --output text --query 'Code.Location'