import sqlite3

from flask import Flask
from flask import jsonify
from flask import request
import mybackend

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate_recommendations():
    start_station_name = request.args.get('startlocation')
    duration_time = request.args.get('timeduration')
    recommendations_amount = request.args.get('k')
    try:
        validate(start_station_name, duration_time, recommendations_amount)
        db = mybackend.Database()
        answers = db.calculate_recommendations(start_station_name, int(duration_time), int(recommendations_amount))
        return jsonify(answers)
    except Exception as e:
        return jsonify('Error %s' % (e.args[0]))



def validate(start_station_name, duration_time, recommendations_amount):
    try:
        int(duration_time)
    except:
        raise ValueError("Please enter valid duration time")
    if int(duration_time) <= 0:
        raise ValueError ("Please enter valid duration time")
    try:
        int(recommendations_amount)
    except:
        raise ValueError ("Please enter valid recommendations amount")
    if int(recommendations_amount) <= 0:
        raise ValueError ("Please enter valid recommendations amount")
    if len(start_station_name) <= 0:
        raise ValueError ("Please enter valid start location")
    return True

if __name__ == '__main__':
    app.run(debug=True)
