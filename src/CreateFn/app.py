import json
import boto3


def lambda_handler(event, context):
    
    client = boto3.client('sqs')
    response = client.send_message(
        QueueUrl = 'https://sqs.us-east-2.amazonaws.com/618758721119/sqs-practice-RawQueue-9TQ7R07SNNU6',
        MessageBody = json.dumps(event["body"]))
    return {
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': json.dumps(response['ResponseMetadata']),
        'message': 'message sent...'
    }