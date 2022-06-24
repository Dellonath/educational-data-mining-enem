'''
Module to create the dataset and save it in raw/data as .parquet and save the query utilized in .sql. 
The name will have the following format: v<VERSION NUMBER>-enem-raw-<DATE>.parquet 

To use, run the following command:
- make dataset sql=<SQL Query>

e.g.:
- make dataset sql="select \* from enem limit 10"

'''

import os
import sys
from datetime import date
from dbconnector import DatabaseConnection

if __name__ == '__main__':
    # arguments
    query = ' '.join(sys.argv[1:])

    # creating dataset name
    NUM_RAW_DATA_FILES = len(list(filter(lambda file: 'csv' in file, os.listdir('data/raw'))))
    DATE_NOW = date.today().strftime('%Y%m%d')
    OUTPUT_PATH = f'data/raw/v{NUM_RAW_DATA_FILES}-enem-raw-{DATE_NOW}'

    # connecting to database
    database = DatabaseConnection()

    # database consult and save the result as .parquet file
    raw_data = database.query(query)
    raw_data.read_csv(OUTPUT_PATH + '.csv', sep = ';')

    # save query as sql file
    text_file = open(OUTPUT_PATH + '-query.sql', "w")
    text_file.write(query)
    text_file.close()
