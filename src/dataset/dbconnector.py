import sqlalchemy
import pandas as pd
import json 
auth = json.load(open('src/authentication.json'))

class DatabaseConnection():
    
    '''
    class just to connect with the database
    '''
    
    def __init__(self):
        self.cnx = sqlalchemy.create_engine(f"mysql+pymysql://{auth['dbuser']}:{auth['dbpassw']}@{auth['dbhost']}/tfg")
        
    def query(self, query):
        
        connection = self.cnx.connect()
        enem_candidates = pd.read_sql_query(query, connection)
        connection.close()
        
        return enem_candidates
