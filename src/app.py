import json
# import os
import boto3


# queue_name = os.environ.get('RawQueue')
def lambda_handler(events, context):

    sqs = boto3.client('sqs')
    queue_url = 'https://sqs.us-east-2.amazonaws.com/618758721119/sqs-practice-RawQueue-9TQ7R07SNNU6'

    response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)


    return{
        'status code': json.dumps(response['MessageId']),
        'body': json.dumps({
            'message': 'Hello from sqs'
        })
    }