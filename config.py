import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    Debug = True
    SECRET_KEY= os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class DevConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://moringa:12345@localhost/blog"

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass

configurations = {"development":DevConfig, "production":ProdConfig}

 