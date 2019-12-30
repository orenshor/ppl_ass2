import csv
import sqlite3
import pandas as pd
import numpy as np
import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('BikeShare.db')
        self.cursor = self.conn.cursor()
        self.init_table()


    def init_table(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS bikeShare (TripDuration INTEGER ,StartTime DATETIME, "
            "StopTime DATETIME, StartStationID INTEGER, StartStationName TEXT, StartStationLatitude REAL,"
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

    def calculate_recommendations(self, start_station_name, duration_time, recommendations_amount):
        df = self.execute_query(start_station_name)
        df = self.scoring_trips(duration_time, recommendations_amount, df)
        print (df)


    def execute_query(self, start_station_name):
        query = "SELECT * FROM bikeShare WHERE StartStationName = '" + start_station_name + "'"
        results = self.cursor.execute(query)
        cols = [column[0] for column in results.description]
        df = pd.DataFrame.from_records(data=results.fetchall(), columns=cols)
        return df

    def scoring_trips(self, duration_time, recommendations_amount, df):
        df2 = df.groupby(['StartStationName', 'EndStationName']).agg({"TripDurationinmin": np.median})
        df2['score'] = np.abs(df2['TripDurationinmin'] - duration_time)
        df2.sort_values(by=['score'], ascending=True, inplace=True)
        df2 = df2.head(recommendations_amount)
        return df2


# + start_station_name + "' AND (TripDurationinmin >= "\
#                 + str(duration_time - duration_time_percent) \
#                 + " AND TripDurationinmin <= " + str(duration_time + duration_time_percent) +")"
if __name__ == "__main__":
    db = Database()
    db.calculate_recommendations('Oakland Ave', 5, 5)
