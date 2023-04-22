from car_resale import parser
from psycopg2 import connect, DatabaseError

class DatabaseConn:

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

    def connect_db():
        """
        To connect with PostGRESql database
        """
        con, cursor = None
        try:   
            dbValues = DatabaseConn.get_config()
            host = dbValues["hostname"]
            database = dbValues["database"]
            user = dbValues["username"]
            password = dbValues["password"]
            port = dbValues["port"]

            with connect(
                            host = host,
                            database = database,
                            user = user,
                            password = password,
                            port = port
                                ) as con:
                    cursor = con.cursor()
            return cursor
        except DatabaseError as e:
            print("Error: ", e)
        finally:
            con.close()

