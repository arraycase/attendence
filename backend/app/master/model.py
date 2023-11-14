from app import db , ma
from marshmallow_sqlalchemy import field_for 

from datetime import datetime

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    details = db.Column(db.JSON, default=None)

class LocationSchema(ma.ModelSchema ):
    class Meta:
        model = Location

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    location = db.r(db.String(250))
    details = db.Column(db.JSON, default=None)
    location = db.relationship('Location', secondary='comp_location',
                                backref='comp_location',  lazy='joined')

class CompanySchema(ma.ModelSchema ):
    class Meta:
        model = Company



db.Table('comp_location',
         db.Column('comp_id', db.Integer, db.ForeignKey(
             'company.id', ondelete='SET NULL')),
         db.Column('location_id', db.Integer, db.ForeignKey(
             'location.id', ondelete='SET NULL'))
         )
