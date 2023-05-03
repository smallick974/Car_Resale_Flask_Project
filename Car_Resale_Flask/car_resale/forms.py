from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField, EmailField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from car_resale.dbConstants import DbConstants
from car_resale.dbModels import DatabaseQueries
from datetime import date
import re

def check_if_only_str(form, field):
    """
        Validator to check if the field has only string value or not. If not raise error
    """
    check = re.match(r'^[a-zA-Z]+$', field.data) 
    if check is None:
        raise ValidationError("must not contain numeric values")
    
def check_addr(form, field):
    """
        Validator to check if address field contains only string, integers and special characters(- , / :)
    """
    check = re.match(r'^[a-zA-z1-9,-:.\s]+$', field.data)
    if check is None:
        raise ValidationError("Must only contain alphanumeric characters and , - : .")

class SignUp(FlaskForm):

    state_list = sorted(list({values for values in DbConstants.STATE_DICT.values()}))
    country_list = sorted(list({values for values in DbConstants.Country_DICT.values()}))

    # Custom validation for various HTML fields
    
    def validate_emailid(self, field):
        result = DatabaseQueries.search_data(DbConstants.TBL_USER, [DbConstants.EMAIL_ID],{DbConstants.EMAIL_ID : field.data})
        if result != [] and result[0][0] == field.data:
            raise ValidationError("This Email ID already exists")

    def validate_password(self, field):
        check = re.match(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$', field.data)
        if check is None:
            raise ValidationError("Password must contain atleast one lowercase, one uppercase, one numeric and one special character in it")

    def validate_dob(self, field):
        age = float((date.today() - field.data).days / (365.25))
        if age < 18:
            raise ValidationError("You must be atleast 18 years of age to Sign Up")
              
    def validate_zipcode(self, field):
        check = re.match(r'^[1-9][0-9]{5}$', str(field.data))
        if check is None:
            raise ValidationError("It must not start with 0 and contain only numeric value") 

    def validate_contact(self, field):
        check = re.match(r'^[789][0-9]{9}$', str(field.data))
        if check is None:
            raise ValidationError("Invalid mobile number (must start with 7,8,9 and should be 10-digits in length)")
        
        result = DatabaseQueries.search_data(DbConstants.TBL_USER, [DbConstants.CONTACT],{DbConstants.CONTACT : str(field.data)})
        if result != [] and result[0][0] == str(field.data):
            raise ValidationError("This contact number already exists")
   

   # Flask Form field that directly maps in HTML form
    firstname = StringField(label="First Name", validators=[Length(min=2, max=30), DataRequired(), check_if_only_str])
    lastname = StringField(label="Last Name", validators=[Length(min=2, max=30), DataRequired(), check_if_only_str])
    emailid = EmailField(label="Email ID", validators=[Email(message="Incorrect Email ID"), DataRequired()])
    password = PasswordField("Password", validators=[Length(min=8, max=25), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[Length(min=8, max=25), DataRequired(), EqualTo('password', message="Password and Confirm Password must match")])
    dob = DateField(label="Date Of Birth", format='%Y-%m-%d', validators=[DataRequired()])
    addr_1 = StringField(label="Address Line 1", validators=[Length(min=2, max=30), DataRequired(), check_addr])
    addr_2 = StringField(label="Address Line 2", validators=[Length(min=2, max=30), DataRequired(), check_addr])
    city = StringField(label="City", validators=[Length(min=2, max=30), DataRequired(), check_if_only_str])
    state = SelectField(label="State", choices=state_list)
    zipcode = StringField(label="Zip Code", validators=[Length(min=6, max=6), DataRequired()])
    country = SelectField(label="Country", choices=country_list)
    contact = IntegerField(label="Mobile Number", validators=[NumberRange(min=1000000000, max=9999999999), DataRequired()])
    submit = SubmitField(label='Sign Up')

