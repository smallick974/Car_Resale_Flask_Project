import functools
from car_resale.dbConstants import DbConstants
from werkzeug.security import generate_password_hash
import datetime

def user_data_mapper(func):
    @functools.wraps(func)
    def user_decorator(user_form_data):
        user_dict = {}
        if "firstname" in user_form_data:
            user_dict[DbConstants.FIRST_NAME] = user_form_data.get("firstname")
        if "lastname" in user_form_data:
            user_dict[DbConstants.LAST_NAME] = user_form_data.get("lastname")
        if "emailid" in user_form_data:
            user_dict[DbConstants.EMAIL_ID] = user_form_data.get("emailid")
        if "password" in user_form_data:
            user_dict[DbConstants.PASSWORD] = generate_password_hash(user_form_data.get("password"))
        if "dob" in user_form_data:
            user_dict[DbConstants.DOB] = user_form_data.get("dob")
        if "addr_1" in user_form_data:
            user_dict[DbConstants.ADDR_1] = user_form_data.get("addr_1")
        if "addr_2" in user_form_data:
            user_dict[DbConstants.ADDR_2] = user_form_data.get("addr_2")
        if "city" in user_form_data:
            user_dict[DbConstants.CITY] = user_form_data.get("city")
        if "state" in user_form_data:
            user_dict[DbConstants.STATE] = user_form_data.get("state")
        if "zipcode" in user_form_data:
            user_dict[DbConstants.ZIP] = user_form_data.get("zipcode")
        if "country" in user_form_data:
            user_dict[DbConstants.COUNTRY] = user_form_data.get("country")
        if "contact" in user_form_data:
            user_dict[DbConstants.CONTACT] = user_form_data.get("contact")  
        user_dict[DbConstants.LAST_LOGIN] =  datetime.datetime.now(datetime.timezone.utc)
        user_dict[DbConstants.USER_TYPE] = "customer"
        return user_dict
    return user_decorator
