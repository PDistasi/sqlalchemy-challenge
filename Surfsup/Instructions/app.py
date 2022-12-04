import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)

# Save reference to the table
meas = base.classes.measurement
stat = base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>Returns a JSON list of Hawaii Precipitation for the dates of 8-23-16 through 8-23-17<br><br>"
        f"/api/v1.0/stations<br/>Returns a JSON list of all stations in Hawaii<br><br>"
        f"/api/v1.0/tobs<br/>Returns a JSON list of the Temperature Observations (tobs) for each station for the dates of 8-23-16 through 8-23-17<br/><br>"
        f"/api/v1.0/date<br/>Returns a JSON list of the Temperature Observations (tobs) maximum, minimum, and avertage for each station for the date input (between 1-1-2010 and 8-23-2017)<br><br>"
        f"/api/v1.0/startdate/enddate<br>Returns a JSON list of the Temperature Observations (tobs) maximum, minimum, and avertage for each station for the start date and end date input (between 1-1-2010 and 8-23-2017)<br><br>"
    )


@app.route("/api/v1.0/precipitation/")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Return a list of Hawaii Precipitation for the most recent 12 months of data"""
    # Query precipitation analysis
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    latest_data = session.query(meas.date, meas.prcp).\
    filter(meas.date >= one_year).\
    order_by(meas.date).all()

    session.close()

    # Convert list of tuples into normal list
    list(np.ravel(latest_data))

    return jsonify(latest_data)


@app.route("/api/v1.0/stations/")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all stations in Hawaii"""
    # Return a JSON list of stations from the dataset
    most_rows = session.query(stat.station, stat.name).all()
    # order_by(func.count(meas.tobs).desc()).all()
    # for station, count in most_rows:
    #     print(station, count)
    
    session.close()
    
    list(np.ravel(most_rows))
    
    return jsonify(most_rows)

   

@app.route("/api/v1.0/tobs/")
def tobs():
    
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #Query the dates and temperature observations of the most-active station for the previous year of data
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    most_rows = session.query(meas.station, func.count(meas.tobs)).group_by(meas.station).\
    order_by(func.count(meas.tobs).desc()).all()
    most_active = most_rows[0][0]
    
    most_active_data = session.query(meas.station, meas.date, meas.tobs).\
    filter(meas.date >= one_year).\
    filter(meas.station == most_active).\
    order_by(meas.date).all()
    
    session.close()
    
    # Convert list of tuples into normal list
    list(np.ravel(most_active_data))

    return jsonify(most_active_data)

@app.route("/api/v1.0/<date>/")
def date(date):
    
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    start_date_stats = session.query(meas.station, func.avg(meas.tobs), func.max(meas.tobs), func.min(meas.tobs)).filter(meas.date >= date).all()
    
    session.close()
    
    list(np.ravel(start_date_stats))

    return jsonify(start_date_stats)


@app.route("/api/v1.0/<start>/<end>/")
def start_end(start, end):
    
     # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
    start_end_stats = session.query(meas.station, func.avg(meas.tobs), func.max(meas.tobs), func.min(meas.tobs)).filter(meas.date >= start).filter(meas.date <= end).all()
    
    session.close()
    
    list(np.ravel(start_end_stats))

    return jsonify(start_end_stats)

#Boilerplate
    
if __name__ == '__main__':
    app.run(debug=True)

