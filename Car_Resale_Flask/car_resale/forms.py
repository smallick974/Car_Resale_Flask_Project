from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from car_resale.dbConstants import DbConstants

class SignUp(FlaskForm):

    state_list = sorted(list({values for values in DbConstants.STATE_DICT.values()}))
   
    firstname = StringField(label="First Name", validators=[Length(min=2, max=30), DataRequired()])
    lastname = StringField(label="Last Name", validators=[Length(min=2, max=30), DataRequired()])
    emailid = StringField(label="Email ID", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[Length(min=8, max=25), DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[Length(min=8, max=25), DataRequired(), EqualTo('password', message="Password must match")])
    dob = DateTimeField(label="Date Of Birth", validators=[DataRequired()])
    addr_1 = StringField(label="Address Line 1", validators=[Length(min=5, max=30), DataRequired()])
    addr_2 = StringField(label="Address Line 2", validators=[Length(min=5, max=30), DataRequired()])
    city = StringField(label="City", validators=[Length(min=2, max=30), DataRequired()])
    state = SelectField(label="State", choices=state_list)
    zipcode = IntegerField(label="Zip Code", validators=[Length(min=6, max=10), DataRequired()])
    country = StringField(label="Country", default="India", render_kw={'readonly': True})
    contact = IntegerField(label="Mobile Number", validators=[Length(min=10), DataRequired()])
    submit = SubmitField(label='Sign Up')

