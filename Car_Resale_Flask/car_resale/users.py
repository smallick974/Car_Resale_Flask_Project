
from car_resale.dbFormMapper import user_data_mapper
from car_resale.dbModels import DatabaseQueries
from car_resale.dbConstants import DbConstants

class Users:

    @user_data_mapper
    def get_mapped_user_data(user_form_data): return
       
    def create_user(user_form_data):
        user_dict = Users.get_mapped_user_data(user_form_data)
        result = DatabaseQueries.insert_data(DbConstants.TBL_USER, user_dict)
        print("Result: ", result)
    