import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    return{
        'body':json.dumps({
            'message': 'message received!!!'
        })
    }
   