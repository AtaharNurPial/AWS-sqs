import json

def lambda_handler(events, context):
    return{
        "status code": 200,
        "body": json.dumps({
            "message": "Hello from sqs"
        })
    }