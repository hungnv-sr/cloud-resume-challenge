import boto3
import json
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

def get_count():
    visitors = table.query(
        KeyConditionExpression=Key('ID').eq('visitors')
    )
    requests = table.query(
        KeyConditionExpression=Key('ID').eq('requests')
    )
    response= {
        "visitors": int(visitors["Items"][0]["visitors"]),
        "requests": int(requests["Items"][0]["requests"])
    }
    return json.dumps(response)

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Credentials': '*',
            'Content-Type': 'application/json'
        },
        'body': get_count()
    }