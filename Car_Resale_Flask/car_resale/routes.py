from car_resale import carapp
from flask_restful import Api
from car_resale.userApi import Users

"""
Class to map API classes with various URls. Acts as an URL Manager.
"""
api = Api(carapp) #creating API object

# URLs for class Users:
api.add_resource(Users,'/login')
