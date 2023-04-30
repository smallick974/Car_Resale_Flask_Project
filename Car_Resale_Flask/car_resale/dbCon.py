from psycopg2 import connect, DatabaseError
from car_resale import parser

"""
    To establish Database connection with PostGRESql database
"""

def get_config():
        """
        To fetch database connection values from config file
        """
        db = {}
        try:
            if 'DATABASE' in parser:
                for key in parser['DATABASE']:
                    db[key] = parser['DATABASE'][key]
                return db
            else:
                raise Exception("Cannot fetch data from config file")
        except Exception as e:
            print("Error: ", e)


class DatabaseConn:
    """
        Context Manager class to create and close database connections
    """
    def __init__(self):
        self.cursor = None
        self.con = None

    def __enter__(self):
        try:   
            dbValues = get_config()
            host = dbValues["hostname"]
            database = dbValues["database"]
            user = dbValues["username"]
            password = dbValues["password"]
            port = dbValues["port"]

            self.con = connect(
                            host = host,
                            database = database,
                            user = user,
                            password = password,
                            port = port
                                )
            self.cursor = self.con.cursor()
            return self.cursor
        except DatabaseError as e:
            print("Error: ", e)

    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.cursor.close()
        self.con.close()