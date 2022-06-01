'''
Module to create the dataset. To use, run the following command:
- python3 make_dataset.py <raw/processed> <SQL Query>

Example:
- python3 make_dataset.py raw "SELECT * FROM tfg.enem"

'''

import os
import sys
from datetime import date
from dbconnector import DatabaseConnection


if __name__ == '__main__':
    # arguments
    query = sys.argv[1]

    # creating dataset name
    NUM_RAW_DATA_FILES = len(list(filter(lambda file: 'parquet' in file, os.listdir('../../data/raw'))))
    date_now = date.today().strftime('%Y%m%d')
    OUTPUT_PATH = f'../../data/raw/v{NUM_RAW_DATA_FILES}-enem-raw-{date_now}'

    # connecting to database
    database = DatabaseConnection()

    # database consult and save the re
    # sult as .parquet file
    raw_data = database.select_query(query)
    raw_data.to_parquet(OUTPUT_PATH + '.parquet', engine = 'fastparquet')

    # save query as sql file
    text_file = open(OUTPUT_PATH + '-query.sql', "w")
    text_file.write(query)
    text_file.close()