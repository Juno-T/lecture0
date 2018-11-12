import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    #Flight.query.filter_by(origin="Paris").first()
    #                                      .count()
    #Flight.query.get(28) ## filter_by(id=28)
    #Flight.query.order_by(Flight.origin).all()
    #Flight.query.order_by(Flight.origin.desc()).all()
    #Flight.query.filter(Flight.origin!="Paris").all() ##filter(%boolean exp%)
    #             filter(Flight.origin.like("%a%")).all()
    #             filter(Flight.origin.in_(["Tokyo","Paris"]])).all()
    #             filter(and_(Flight.origin=="Paris",Flight.duration > 500)).all()
    #                    or_
    #db.session.query(Flight,Passenger).filter(Flight.id == Passenger.flight_id).all()
                                                    ##SELECT * FROM flights JOIN passenger ON ...
    #flights.duration = 280  ## Update column
    #db.session.delete(flight(s)) ## Delete row(s)
    #
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


if __name__ == "__main__":
    with app.app_context():
        main()
