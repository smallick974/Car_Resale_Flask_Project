from flask_restful import Resource
from flask import jsonify, request


""""
Contains User related API classes and functions for SignUp, Login, Logout, etc...
"""

login={
    'emailid' : 'smallick974@gmail.com',
    'username' : 'srijan',
    'password' : 'srijan'
}

class Users(Resource):

    def post(self):
        # emailid = request.args.get('emailid')    # for GET method
        # password = request.args.get('password') # for POST method

        emailid = request.form['emailid']
        password = request.form['password']

        if emailid == login['emailid'] and password == login['password']:
            return jsonify({'Hi' : login['username']})
        else:
            return jsonify({'Error message' : 'Incorrect Username or password'})

