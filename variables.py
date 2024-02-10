from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
from os import environ
from dotenv import load_dotenv

# leerael archivo .env si existe y agregara todas las variables al entorno como
# si fuesen variables de entorno del sistema
# tiene que ir en la parte mas alta del archivo principalpara que pueda ser
# utilizado en todo el proyecto
load_dotenv()


conexion = SQLAlchemy()

clienteTwilio = Client(username=environ.get('TWILIO_ACCOUNT_SID'),
                       password = environ.get('TWILIO_AUTH_TOKEN'))