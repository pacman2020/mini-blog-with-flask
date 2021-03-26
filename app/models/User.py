from app import db
import hashlib

class UserModel(db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    
    def __repr__(self) -> str:
        return f'{self.username}'
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    def hash_password(self):
        self.password = hashlib.sha256(str.encode(self.password)).hexdigest()
    
    def check_hash(self, password):
        if hashlib.sha256(str.encode(password)).hexdigest() == self.password:
            return True
        return False
    
    def find_email(self):
        pass
    
    @classmethod  
    def find_by_user(cls, id):
        user = UserModel.query.get(id)
        if user:
            return user
        return None
    
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()