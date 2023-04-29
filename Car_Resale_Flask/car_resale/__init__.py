from flask import Flask
from configparser import ConfigParser

carapp = Flask(__name__)

# To read config file and get the values
parser = ConfigParser()
parser.read('prjconfigs.cfg')

# to get the value of secret key and convert the returned values from list to string using ''.join()
secret_key = ''.join([parser['SECRET_KEY'][key] for key in parser['SECRET_KEY'] if 'SECRET_KEY' in parser])

carapp.config['SECRET_KEY'] = secret_key

from car_resale import routes

