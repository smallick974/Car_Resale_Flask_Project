from psycopg2 import ProgrammingError, InterfaceError, DatabaseError
from car_resale.dbCon import DatabaseConn

class DatabaseQueries:

    """
    Class to query database and fetch values from tables    
    """

    def insert_data(table_name, data_dict):
        try:
            with DatabaseConn() as cursor:
                query = "insert into car."+ table_name + "(" + \
                            ",".join(data_dict.keys()) + ")" + \
                                " values(" + ",".join(["%s"] * len(data_dict.keys())) + ")"
                cursor.execute(query, list(data_dict.values()))
                return True

        except DatabaseError as e:
            print("Error: ", e)

    def search_data(table_name,column_name_list,data_dict):
        try:
            with DatabaseConn() as cursor:   
                if data_dict == {}:
                    query = "select " + ",".join(column_name_list) +" from car."+ table_name
                else:
                    query = "select " + ",".join(column_name_list) +" from car."+ table_name + \
                                " where " + " and ".join(name +" = " +"'"+data_dict[name]+"'" for name in data_dict)
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print("Exception: ", e)

    
        