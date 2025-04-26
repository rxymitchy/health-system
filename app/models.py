from datetime import datetime
from app import db

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    clients = db.relationship('Client', secondary='enrollments', back_populates='programs')

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    programs = db.relationship('Program', secondary='enrollments', back_populates='clients')

enrollments = db.Table('enrollments',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey('program.id'), primary_key=True),
    db.Column('enrolled_at', db.DateTime, default=datetime.utcnow)
)