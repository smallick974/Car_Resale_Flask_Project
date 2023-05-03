

class DbConstants:
    """
    This class contains mapping of database columns with the Python Constant variables so that direct database table column names
    are not used in program.
    Add/Modify in case of any changes in database tables.
    """

    # tblUser constants:
    TBL_USER = "tbluser"
    FIRST_NAME = "firstname"
    LAST_NAME = "lastname"
    EMAIL_ID = "emailid"
    PASSWORD = "pass"
    DOB = "dob"
    ADDR_1 = "addr_1"
    ADDR_2 = "addr_2"
    CITY = "city"
    STATE = "states"
    ZIP = "zip"
    COUNTRY = "country"
    CONTACT = "contact"
    LAST_LOGIN = "last_login"
    USER_TYPE = "user_type"

    # Other constants:
    STATE_DICT = {'AN':'Andaman and Nicobar Islands','AP':'Andhra Pradesh','AR':'Arunachal Pradesh','AS':'Assam','BR':'Bihar','CH':'Chandigarh','CG':'Chhattisgarh','DH':'Dadra and Nagar Haveli',
    'DD':'Daman and Diu','DL':'Delhi','GA':'Goa','GJ':'Gujarat','HR':'Haryana','HP':'Himachal Pradesh','JK':'Jammu and Kashmir','JH':'Jharkhand','KA':'Karnataka','KL':'Kerala','LD':'Lakshadweep',
    'MP':'Madhya Pradesh','MH':'Maharashtra','MN':'Manipur','ML':'Meghalaya','MZ':'Mizoram','NL':'Nagaland','OR':'Orissa','PY':'Pondicherry','PB':'Punjab','RJ':'Rajasthan','SK':'Sikkim',
    'TN':'Tamil Nadu','TR':'Tripura','UP':'Uttar Pradesh','UK':'Uttarakhand','WB':'West Bengal'}

    Country_DICT = {'IN' : 'India'}

     