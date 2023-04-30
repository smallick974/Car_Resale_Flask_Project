from flask_restful import Resource
from flask import jsonify, request, render_template, make_response, redirect, url_for, flash
from car_resale.dbModels import DatabaseQueries
from car_resale.forms import SignUp
from car_resale.users import Users
import datetime

headers = {'Content-Type': 'text/html'}

""""
Contains API classes and functions for Users, Cars, etc...
"""

login={
    'emailid' : 'smallick974@gmail.com',
    'username' : 'srijan',
    'password' : 'srijan'
}

class Welcome(Resource):
    def get(self):
        return make_response(render_template("Welcome.html"), headers)

class UserSignUp(Resource):
     def __init__(self):
         self.form = SignUp()

     def get(self):
         return make_response(render_template("SignUp.html", form=self.form), headers)

     def post(self):
        
            # firstname = self.form.firstname.data
            # lastname = self.form.lastname.data
            # emailid = self.form.emailid.data
            # password = generate_password_hash(self.form.password.data)
            # dob = self.form.dob.data
            # addr_1 = self.form.addr_1.data
            # addr_2 = self.form.addr_2.data
            # city = self.form.city.data
            # state = self.form.state.data
            # zipcode = self.form.zipcode.data
            # country = self.form.country.data
            # contact = self.form.contact.data
            # last_login =  datetime.datetime.now(datetime.timezone.utc)
            
            if self.form.errors !={}:
                for err in self.form.errors.values():
                    flash(f'There was an error: {err}', category='danger')
                    
            data = Users.create_user(request.form)

            return make_response(redirect(url_for('mainpage')), headers)

class UserSignIn(Resource):

    def post(self):
        # emailid = request.args.get('emailid')    # for GET method
        # password = request.args.get('password') # for POST method

        emailid = request.form['emailid']
        password = request.form['password']

        if emailid == login['emailid'] and password == login['password']:
            return jsonify({'Hi' : login['username']})
        else:
            return jsonify({'Error message' : 'Incorrect Username or password'})
        
class SearchData(Resource):
    def get(self):
        result = DatabaseQueries.search_data()
        print(result)

