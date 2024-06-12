import boto3
import io

s3 = boto3.client("s3")
bucket_name = "e-commerce-daily-data"


def upload_to_s3(filename, year, month, day, csv_buffer):
    file_path = f"transactions/year={year}/month={month}/day={day}/{filename}"  
    
    s3.upload_fileobj(csv_buffer, bucket_name, file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return