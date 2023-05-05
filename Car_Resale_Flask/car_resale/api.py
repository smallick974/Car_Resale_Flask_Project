from flask_restful import Resource
from flask import jsonify, request, render_template, make_response, redirect, url_for, flash
from car_resale.dbModels import DatabaseQueries
from car_resale.forms import SignUp, SignIn
from car_resale.users import Users
from flask_login import login_user, logout_user, login_required, current_user

headers = {'Content-Type': 'text/html'}

""""
Contains API classes and functions for Users, Cars, etc...
"""

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
            flash('Account created successfully. Please Log in to continue', category='info')
            return make_response(redirect(url_for('login')), headers)
                        
        if self.form.errors !={}:
                for key, value in self.form.errors.items():
                    flash(f'Please correct the following error -> {key} : {value}', category='danger')    
                             
        return make_response(render_template('SignUp.html', form=self.form), headers)

class UserSignIn(Resource):
    def __init__(self):
        self.form = SignIn()

    def get(self):
        return make_response(render_template("Login.html", form=self.form), headers)
    
    def post(self): 
        if self.form.validate_on_submit():
            user = Users()
            signed_in_user = user.sign_in(request.form)
            if signed_in_user:
                login_user(user)
                flash(f'Welcome {current_user.firstname} {current_user.lastname}', category='success')  
                return make_response(redirect(url_for('mainpage')), headers)   
            else:
                flash('Incorrect Username or Password..', category='warning')
                        
        if self.form.errors !={}:
                for key, value in self.form.errors.items():
                    flash(f'Please correct the following error -> {key} : {value}', category='danger')    
                             
        return make_response(render_template('Login.html', form=self.form), headers)

class UserLogout(Resource):
    def get(self):
        logout_user()
        flash('You have been logged out', category='info')
        return make_response(redirect(url_for('mainpage')), headers)


class SearchData(Resource):
    def get(self):
        result = DatabaseQueries.search_data()
        print(result)

