from app import db

class PublicationModel(db.Model):
    __tablename__='publications'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    img = db.Column(db.String())
    data = db.Column(db.LargeBinary)
    description = db.Column(db.Text, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))