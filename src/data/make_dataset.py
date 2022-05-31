import os
from datetime import date
from dbconnector import DatabaseConnection

query = '''SELECT 
    * 
FROM tfg.enem 
WHERE 
    rand() < 0.1
'''

# destiny data
DATA_DIRECTORY = 'raw'

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