from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', default='sqlite:///:memory:')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS',default=True)
    SECRET_KEY = os.getenv('SECRET_KEY', default='test123')

class Development(DefaultConfig):
    DEBUG = True

class Production(DefaultConfig):
    DEBUG = False


config = {
    'development' : Development,
    'production' : Production
}