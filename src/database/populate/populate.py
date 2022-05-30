'''
This script is responsible to populate the MySQL database. It's require some arguments like
data path, selected columns, table name and the local database password.

To use:
- python3 main.py /path/to/data /path/to/selected_columns table_name password

An exemple:
- python3 main.py enem2019.csv enem_columns.txt enem ********

Developer: Douglas Oliveira
'''

# imports
import pandas as pd
import numpy as np
import mysql.connector
import tqdm as tqdm
import sys

# arguments
# directory of data in .csv format
directory_data = sys.argv[1]
# selected columns
directory_columns = sys.argv[2]
# table name
table = sys.argv[3]
# password for local database
db_password = sys.argv[4]

# formating selected columns input
with open(directory_columns, 'r') as f:
    selected_columns = list(filter(('').__ne__, f.read().split('\n')))

# reading data with pandas.read_csv
data = pd.read_csv(directory_data, sep = ';', usecols = selected_columns, error_bad_lines = False)[selected_columns]

# connecting with database
mydb = mysql.connector.connect(user = 'root', 
                               password = db_password,
                               host = 'localhost',
                               database = 'tfg')
mycursor = mydb.cursor()

# converting data to correct format for insert in database
def convert_data(value):
    if type(value) == np.int64: return int(value)
    elif type(value) == np.float64: return float(value)
    return str(value)

# creating % to sql query
input_values = ''.join(["%s, " for i in range(len(selected_columns))])[:-2]
sql = f'INSERT INTO {table} VALUES ({input_values})'

# populating database
for j in tqdm.tqdm(range(data.shape[0])):
    val = [convert_data(i) if not pd.isna(i) else None for i in data.iloc[j]]
    mycursor.execute(sql, val)
    mydb.commit()

# closing connection with database
mydb.close()
