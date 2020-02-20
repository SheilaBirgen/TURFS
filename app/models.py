from app import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    '''
    reloads the user from the session
    '''
    
class User(db.Model,UserMixin):
    id = db.Column(db.Interger,primary_key=True)
    email = db.Column(db.String(255),unique = True,index = True)
    username = db.Column(db.String(30),index = True)
    password_hash = db.Column(db.String)
    pass_secure = db.Column(db.String(255))