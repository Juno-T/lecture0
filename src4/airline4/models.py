import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    passengers = db.relationship("Passenger", backref="flight", lazy=True) ###
    ## now can use
    ## Flight.query.get(1).passenger
    ## instead of passengers.query.filter_by(flight_id=1).all()
    ## or Passenger.query.filter_by(name="Alice").first().flight
    ## instead of db.session.query(Flight,Passenger).filter(and_(Flight.id == Passenger.flight_id,Passenger.name=="Alice")).all()
    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
