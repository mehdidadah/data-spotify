from datetime import datetime
import csv

from dal import insert
from db import Database


def extract(filepath):
    # Extract data with specific columns
    data = []
    try:
        with open(filepath, encoding='latin1') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # skip header row
            for row in reader:
                # remove commas between double-quotes, replace double-quotes with nothing
                cleaned_row = [field.replace(',', '').replace('"', '') for field in row]
                data.append(tuple(cleaned_row[1:29]))
        return data
    except Exception as e:
        print(e)


def transform(data):
    transformed_data = []

    for row in data:
        release_date = row[2]

        date_formats = ["%m/%d/%Y", "%M/%d/%Y", "%m/%d/%y"]
        year = None

        for fmt in date_formats:
            try:
                year = datetime.strptime(release_date, fmt).year
                break
            except ValueError:
                continue

        tiktok_likes = int(row[4]) if row[4] else 0

        track = row[0]
        artist = row[1]
        track_score = row[3]

        transformed_data.append((year, tiktok_likes, track, artist, track_score))

    return transformed_data


def load(transformed_data):
    # Insert transformed_data into the database
    insert(transformed_data)
    #db = Database("db_spotify")
    #db.write(transformed_data, 'spotify')


def etl_process(filepath):
    data = extract(filepath)
    if data is None:
        print("Error: Unable to extract data from the file.")
        return
    data = transform(data)
    load(data)
