import csv
import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('BikeShare.db')
        self.cursor = self.conn.cursor()
        self.init_table()

    def init_table(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS bikeShare (TripDuration INTEGER ,StartTime TIMESTAMP, "
            "StopTime TIMESTAMP, StartStationID INTEGER, StartStationName TEXT, StartStationLatitude REAL,"
            " StartStationLongitude REAL, EndStationID INTEGER, EndStationName TEXT, EndStationLatitude REAL,"
            " EndStationLongitude REAL, BikeID INTEGER, UserType TEXT, BirthYear INTEGER, Gender"
            " INTEGER, TripDurationinmin INTEGER)")
        self.conn.commit()

        with open('BikeShare.csv', 'r') as f:
            reader = csv.reader(f)
            data = next(reader)
            query = 'insert into bikeShare values ({0})'
            query = query.format(','.join('?' * len(data)))
            self.cursor.execute(query, data)
            for data in reader:
                self.cursor.execute(query, data)
            self.conn.commit()

    def execute_query(self, start_station_name, duration_time):
        query = "SELECT * FROM bikeShare WHERE StartStationName = '" + start_station_name + "' AND TripDurationinmin = "
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for res in results:
            print(res)

if __name__ == "__main__":
    db = Database()
    db.execute_query('Christ Hospital', 5)
