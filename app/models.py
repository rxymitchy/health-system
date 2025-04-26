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
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    programs = db.relationship('Program', secondary='enrollments', back_populates='clients')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

enrollments = db.Table('enrollments',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id')),
    db.Column('program_id', db.Integer, db.ForeignKey('program.id')),
    db.Column('enrollment_date', db.DateTime, default=datetime.utcnow),
    db.Column('is_active', db.Boolean, default=True)
)

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    notes = db.Column(db.Text)
    
    # Relationships
    client = db.relationship('Client', backref='enrollments')
    program = db.relationship('Program', backref='enrollments')