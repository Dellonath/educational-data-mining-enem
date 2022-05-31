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

# arguments
DATA_DIRECTORY = sys.argv[0]
query = sys.argv[1]

# num .parquet files in data\raw
NUM_RAW_DATA_FILES = len(list(filter(lambda file: 'parquet' in file, os.listdir(f'data\\{DATA_DIRECTORY}'))))
DATE_NOW = date.today().strftime('%Y%m%d')
DATASET_DIRECTORY = f'data\\{DATA_DIRECTORY}\\v{NUM_RAW_DATA_FILES}-enem-{DATA_DIRECTORY}-{DATE_NOW}'

# connecting to database
database = DatabaseConnection()

# database consult and save the re
# sult as .parquet file
raw_data = database.select_query(query)
raw_data.to_parquet(DATASET_DIRECTORY + '.parquet', engine = 'fastparquet')

# save query as sql file
text_file = open(DATASET_DIRECTORY + '-query.sql', "w")
text_file.write(query)
text_file.close()