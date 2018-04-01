import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=file_name)
    jsonfileredor = json_object['Body'].read()
    jsonDist = json.loads(jsonfileredor)
    table = dynamodb.Table('emplyoes')
    table.put_item(Item=jsonDist)
    print(str(event))
