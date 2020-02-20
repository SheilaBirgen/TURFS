import os
class Config:
    '''
    General configurations parent class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/turfs'
    
    # email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''  
    
    SECRET_KEY = 'tuf'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/turfs'
    DEBUG = True
    ENV = 'developmet'
    
config_options = {
    'development':DevConfig,
    'production' :ProdConfig
}     
    

