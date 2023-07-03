#!/bin/bash

serverless invoke local -f predict --stage local --path ./test/sqs-message-fixture.json