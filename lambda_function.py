import json 
from datetime import date,timedelta
from generate_mock_data import generate_mock_data
from upload_to_s3 import upload_to_s3
import io
import csv

start_date = date(2024, 5, 13)
end_date = date(2024, 6, 12)

number_of_transactions_everyday = 10
def lambda_handler(event, context):

    current_date = start_date
    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        day = current_date.day
        print(current_date, year, month, day)

        file_name = f"transactions_{current_date.strftime('%Y-%m-%d')}.csv"
        print(file_name)

        data = generate_mock_data(current_date.strftime("%Y-%m-%d"),number_of_transactions_everyday)
        print(data)


        csv_buffer = io.StringIO()
        writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        csv_buffer.seek(0)
        csv_data = csv_buffer.getvalue()

        csv_bytes = csv_data.encode("utf-8") 

        # Create a BytesIO object
        csv_buffer = io.BytesIO(csv_bytes) 

        upload_to_s3(file_name, year, month, day, csv_buffer)

        current_date += timedelta(days=1)

    return {
        'statusCode': 200,
        'body': json.dumps('Mock data generation and upload completed successfully.')
    }
