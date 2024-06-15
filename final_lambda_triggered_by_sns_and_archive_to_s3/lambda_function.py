import json
import boto3

source_bucket_name = 'e-commerce-daily-data'
destination_bucket_name = 'ecommerce-transactions-archives'

def lambda_handler(event, context):
    
    print(f"Event: {event}")

    # Extract the message from the SNS notification
    message = json.loads(event['Records'][0]['Sns']['Message'])

    # Access the "detail" dictionary within the message
    detail = message['detail']

    # Extract the value of the "state" key
    glue_job_status = detail['state']

    print(f"Glue Job Status: {glue_job_status}")

    if glue_job_status == 'SUCCEEDED':
        if not source_bucket_name:
            return {
                'statusCode': 400,
                'body': json.dumps('Missing source bucket name in event')
            }

        # Create S3 client
        s3 = boto3.client('s3')

        try:
            # Call transfer-files function (defined below)
            transfer_files(s3, source_bucket_name, destination_bucket_name)
            return {
                'statusCode': 200,
                'body': json.dumps('Files transferred successfully')
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error transferring files: {e}')
            }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Glue job {glue_job_status}: {event}")
        }

def transfer_files(s3, source_bucket, destination_bucket):
    for obj in s3.list_objects_v2(Bucket=source_bucket)['Contents']:
        source_key = obj['Key']
        destination_key = source_key  # Copy the entire source key 
        
        # Optional: Modify destination_key if needed (e.g., rename file)
        
        s3.copy_object(CopySource={'Bucket': source_bucket, 'Key': source_key},
                    Bucket = destination_bucket, key = destination_key)
        print(f"Copied {source_key} to {destination_bucket}/{destination_key}")