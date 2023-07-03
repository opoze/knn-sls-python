#!/bin/bash

# echo -n '{"Records":[{"messageId":"9a9fcd60-cd49-4bb5-9ea2-8b6911fdd9f6","body":"{\"Message\":{\"subject_id\":\"3\",\"vital_signs\":[85.0,35.7,99.0]}}"}]}' | base64
# eyJSZWNvcmRzIjpbeyJtZXNzYWdlSWQiOiI5YTlmY2Q2MC1jZDQ5LTRiYjUtOWVhMi04YjY5MTFmZGQ5ZjYiLCJib2R5Ijoie1wiTWVzc2FnZVwiOntcInN1YmplY3RfaWRcIjpcIjNcIixcInZpdGFsX3NpZ25zXCI6Wzg1LjAsMzUuNyw5OS4wXX19In1dfQ==

awslocal lambda invoke \
  --function-name master-degree-serverless-dev-predict \
  --payload eyJSZWNvcmRzIjpbeyJtZXNzYWdlSWQiOiI5YTlmY2Q2MC1jZDQ5LTRiYjUtOWVhMi04YjY5MTFmZGQ5ZjYiLCJib2R5Ijoie1wiTWVzc2FnZVwiOntcInN1YmplY3RfaWRcIjpcIjNcIixcInZpdGFsX3NpZ25zXCI6Wzg1LjAsMzUuNyw5OS4wXX19In1dfQ== \
  output.json