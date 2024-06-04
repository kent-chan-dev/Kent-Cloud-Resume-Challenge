import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kent-cloud-resume-stats')

def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'id': '1'
        },
        UpdateExpression='ADD #views :increment',
        ExpressionAttributeNames={
            '#views': 'views'
        },
        ExpressionAttributeValues={
            ':increment': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    print(response['Attributes']['views'])
    return {
        "statusCode": 200,
        "body": {"views": response['Attributes']['views']},
        "headers": {
            'Content-Type': 'application/json',
        }
    }