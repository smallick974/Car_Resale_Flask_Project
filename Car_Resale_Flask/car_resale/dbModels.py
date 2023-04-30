from psycopg2 import ProgrammingError, InterfaceError, DatabaseError
from car_resale.dbCon import DatabaseConn

class DatabaseQueries:

    """
    Class to query database and fetch values from tables    
    """

    def insert_data(table_name, data_dict):
        try:
            with DatabaseConn() as cursor:
                print("Cursor: ", cursor)
                query = "insert into car."+ table_name + "(" + \
                            ",".join(data_dict.keys()) + ")" + \
                                " values(" + ",".join(["%s"] * len(data_dict.keys())) + ")"

                print(query)
                print(list(data_dict.values()),)
                cursor.executemany(query, (list(data_dict.values()),))
                return True
        except DatabaseError as e:
            print("Error: ", e)

    def search_data():
        try:
            with DatabaseConn() as cursor:   
                cursor.execute("select * from car.tblUser")
                result = cursor.fetchall()
                print(result)
        except InterfaceError as e:
            print("InterfaceError: ", e)
        except ProgrammingError as e:
            print("ProgrammingError: ", e)

        