#!/bin/bash

awslocal sqs send-message --queue-url http://localhost:4566/000000000000/predict-queue --message-body "{\"subject_id\":\"1\", \"vital_signs\":[60.0, 34.7, 99.0]}"
