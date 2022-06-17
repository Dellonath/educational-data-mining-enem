
'''
Script to read some data in .csv format (; separated) and insert it in a table.

To run, execute the following command:
- make populate dir=<DATA DIRECTORY.csv> pass=<DB PASSWORD> host=<DB HOST> table=<TABLE TO INSERT DATA>

e.g.:
- make populate dir="data.csv" pass="**********" host="192.1**.***.***" table="tfg.enem"
'''

# imports
import pandas as pd
import numpy as np
import mysql.connector
import tqdm as tqdm
import sys
import json 
auth = json.load(open('src/authentication.json'))


# arguments
# directory of data in .csv format
directory_data = sys.argv[1]
# password for local database
db_password = sys.argv[2]
# host
host = sys.argv[3]
# table to import data
table = sys.argv[4]

# reading data with pandas.read_csv
data = pd.read_csv(directory_data, sep = ';', encoding='latin-1')

# connecting with database
mydb = mysql.connector.connect(user = auth['dbuser'], 
                               password = auth['dbpassw'],
                               host = auth['dbhost'],
                               database = 'tfg')
mycursor = mydb.cursor()

# converting data to correct format for insert in database
def convert_data(value):
    if type(value) == np.int64: return int(value)
    elif type(value) == np.float64: return float(value)
    return str(value)

# creating % to sql query
input_values = ''.join(["%s, " for i in range(len(data.columns))])[:-2]
sql = f'INSERT INTO {table} VALUES ({input_values})'

# populating database
for j in tqdm.tqdm(range(data.shape[0])):
    val = [convert_data(i) if not pd.isna(i) else None for i in data.iloc[j]]
    mycursor.execute(sql, val)
    mydb.commit()

# closing connection with database
mydb.close()
