import json
import boto3
import os
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    title = body['title']
    gender = body['gender']
    content = body['content']

    item = {
        'id': str(uuid.uuid4()),
        'title': title,
        'gender': gender,
        'content': content
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': '投稿が保存されました。'})
    }
