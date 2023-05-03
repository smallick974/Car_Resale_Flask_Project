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
        if self.form.validate_on_submit():
            data = Users.create_user(request.form)
            return make_response(redirect(url_for('login')), headers)
                        
        if self.form.errors !={}:
                for key, value in self.form.errors.items():
                    flash(f'Please correct the following error -> {key} : {value}', category='danger')    
                             
        return make_response(render_template('SignUp.html', form=self.form), headers)

class UserSignIn(Resource):

    def get(self):
        return make_response(render_template("Login.html"), headers)
              
class SearchData(Resource):
    def get(self):
        result = DatabaseQueries.search_data()
        print(result)

