import boto3
import tempfile

s3 = boto3.client("s3")
bucket_name = "e-commerce-daily-data"


def upload_to_s3(filename, year, month, day, csv_data):
    file_path = f"transactions/year={year}/month={month}/day={day}/{filename}"  

    # Write the CSV data to a temporary file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write(csv_data)
        temp_file.flush()  # Ensure data is written to the file

    
    s3.upload_file(temp_file.name, bucket_name, file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return