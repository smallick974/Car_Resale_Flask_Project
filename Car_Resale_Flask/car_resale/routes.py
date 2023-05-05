from car_resale import carapp
from flask_restful import Api
from car_resale.api import UserSignIn, SearchData, UserSignUp, Welcome, UserLogout

"""
Class to map API classes with various URls. Acts as an URL Manager.
"""
api = Api(carapp) #creating API object

#URLs for Homepage:
api.add_resource(Welcome,'/','/home',endpoint='mainpage')

# URLs for class Users:   
api.add_resource(UserSignUp,'/signup',endpoint='usersignup')
api.add_resource(UserSignIn,'/login', endpoint='login')
api.add_resource(UserLogout,'/logout',endpoint='logout')


# For searching
api.add_resource(SearchData,'/search')
