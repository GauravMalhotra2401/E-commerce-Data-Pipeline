import json 
from datetime import date,timedelta
from generate_mock_data import generate_mock_data
import pandas as pd
from upload_to_s3 import upload_to_s3

start_date = date(2024, 5, 13)
end_date = date(2024, 6, 12)

number_of_transactions_everyday = 50
def lambda_handler(event, context):

    current_date = start_date
    while current_date <= start_date:
        year = current_date.year
        month = current_date.month
        day = current_date.day
        print(current_date, year, month, day)

        file_name = f"transactions_{current_date.strftime("%Y-%m-%d")}.csv"
        print(file_name)

        data = generate_mock_data(current_date.strftime("%Y-%m-%d"), file_name, number_of_transactions_everyday)
        print(data)

        df = pd.DataFrame(data)

        csv_data = df.to_csv(index = False)

        upload_to_s3(file_name, year, month, day, csv_data)

        current_date += timedelta(days=1)
