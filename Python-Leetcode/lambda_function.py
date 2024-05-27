import boto3
import requests
import json
import pandas as pd

# AWS Configuration
timestream_client = boto3.client('timestream-write',
                                aws_access_key_id='AKIA3FLD2VGR5N5MRHOJ',
                                aws_secret_access_key='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',
                                region_name='us-east-1')
database_name = 'stock_market_db'
table_name = 'stock_data'

# API Configuration
api_key = '65Y8HCBTLYM7B4D6'
base_url = 'https://www.alphavantage.co/query'

def fetch_stock_data():
    symbols_input = "HOOD,TSLA,QQQ"
    symbols = [symbol.strip() for symbol in symbols_input.split(',')]

    for symbol in symbols:
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '1min',
            'apikey': api_key
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        records = []
        for timestamp, values in data['Time Series (1min)'].items():
            record = {
                'Dimensions': [
                    {'Name': 'symbol', 'Value': symbol},
                    {'Name': 'interval', 'Value': '1min'}
                ],
                'MeasureName': 'stock_price',
                'MeasureValue': values['4. close'],
                'MeasureValueType': 'DOUBLE',
                'Time': str(int(pd.Timestamp(timestamp).timestamp() * 1000))
            }
            records.append(record)

        try:
            result = timestream_client.write_records(
                DatabaseName=database_name,
                TableName=table_name,
                Records=records,
                CommonAttributes={}
            )
            print("WriteRecords Status for", symbol, ":", result['ResponseMetadata']['HTTPStatusCode'])
        except timestream_client.exceptions.RejectedRecordsException as err:
            print("RejectedRecords: ", err)
            for rr in err.response["RejectedRecords"]:
                print("Rejected Index " + str(rr["RecordIndex"]) + ": " + rr["Reason"])
            print("Other records were written successfully. ")
        except Exception as err:
            print("Error:", err)

if __name__ == "__main__":
    fetch_stock_data()
