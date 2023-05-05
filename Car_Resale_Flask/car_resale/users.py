
from car_resale.dbFormMapper import user_data_mapper
from car_resale.dbModels import DatabaseQueries
from car_resale.dbConstants import DbConstants
from werkzeug.security import check_password_hash
from car_resale import login_manager

@user_data_mapper
def get_mapped_user_data(user_form_data): return

@login_manager.user_loader
def load_user(emailid):
    user = Users()
    user.get_user_details(emailid)
    return user

class Users:
    firstname = None
    lastname = None
    emailid = None
    last_login = None
    user_type = None

    def create_user(user_form_data):
        try:
            user_dict = get_mapped_user_data(user_form_data)
            result = DatabaseQueries.insert_data(DbConstants.TBL_USER, user_dict)
        except Exception as e:
            print("Error: ", e)

    def sign_in(self, user_form_data):
        try:
            user_dict = {DbConstants.EMAIL_ID : user_form_data.get('emailid')}
            column_list = [DbConstants.FIRST_NAME, DbConstants.LAST_NAME, DbConstants.EMAIL_ID, \
                            DbConstants.LAST_LOGIN, DbConstants.USER_TYPE]
            
            db_password_hash = DatabaseQueries.search_data(DbConstants.TBL_USER, [DbConstants.PASSWORD], user_dict)
            chk_password = check_password_hash(db_password_hash[0][0], user_form_data.get('password'))

            if chk_password:
                user = DatabaseQueries.search_data(DbConstants.TBL_USER, column_list, user_dict)
                self.firstname = user[0][0]
                self.lastname = user[0][1]
                self.emailid = user[0][2]
                self.last_login = user[0][3]
                self.user_type = user[0][4]
                return user
            else:
                return None
        except Exception as e:
            print("Error: ", e)

    def get_user_details(self, emailid):
        try:
            user = DatabaseQueries.search_data(DbConstants.TBL_USER, [DbConstants.FIRST_NAME, DbConstants.LAST_NAME, \
                        DbConstants.EMAIL_ID, DbConstants.LAST_LOGIN, DbConstants.USER_TYPE], {DbConstants.EMAIL_ID : emailid})
            
            self.firstname = user[0][0]
            self.lastname = user[0][1]
            self.emailid = user[0][2]
            self.last_login = user[0][3]
            self.user_type = user[0][4]
            return user
        except Exception as e:
            print("Error: ", e)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):   
        return True           

    @property
    def is_anonymous(self):
        return False  
            
    def get_id(self):        
        return self.emailid
    
    def __str__(self):
        return f"<firstname: {self.firstname}, lastname: {self.lastname}, emailid: {self.emailid}, lastlogin: {self.last_login}, usertype: {self.user_type}>"

    def __repr__(self):
        return self.__str__()

            
