import sqlalchemy
import pandas as pd

class DatabaseConnection():
    
    '''
    class just to connect with the database
    '''
    
    def __init__(self, user = 'root', passw = 'mydbpass'):
        self.cnx = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{passw}@localhost/tfg')
        
    def query(self, query):
        
        connection = self.cnx.connect()
        enem_candidates = pd.read_sql_query(query, connection)
        connection.close()
        
        return enem_candidates
