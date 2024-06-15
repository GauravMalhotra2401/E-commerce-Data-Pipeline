import json
import boto3

def lambda_handler(event, context):
    
    s3_event = event['Records'][0]['eventName']
    
    if s3_event == "ObjectCreated:Put":
    
        glue = boto3.client('glue')
        glue_job_name = "ecommerce-job"
        
        try:
            response = glue.start_job_run(JobName = glue_job_name)
            job_run_id = response['JobRunId']
            print(f"Started Glue job {glue_job_name} with run ID : {job_run_id}")
        
        except Exception as e:
            print(f"Error starting Glue job : {e}")
            raise e
            
        
        return {
            'statusCode':200,
            'body':f"Glue job {glue_job_name} started successfully!"
        }
        
    else:
        return {
            'statusCode':400,
            'body':json.dumps(f"Glue job not started")
        }