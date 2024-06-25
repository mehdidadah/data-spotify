from datetime import datetime
import csv
import pandas as pd

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
                data.append(tuple(cleaned_row[0:29]))
        return data
    except Exception as e:
        print(e)


def transform(data):
    transformed_data = []

    for row in data:
        release_date = row[3]

        date_formats = ["%m/%d/%Y", "%M/%d/%Y", "%m/%d/%y"]
        year = None

        for fmt in date_formats:
            try:
                year = datetime.strptime(release_date, fmt).year
                break
            except ValueError:
                continue

        tiktok_likes = int(row[14]) if row[14] else 0

        track = row[0]
        artist = row[2]
        track_score = row[6]

        transformed_data.append((track, artist, year, track_score, tiktok_likes))

    return transformed_data


def load(transformed_data):
    # Insert transformed_data into the database
    # insert(transformed_data)
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(transformed_data, columns=['track', 'artist', 'release_date(year)', 'track_score', 'tiktok_likes'])
    db = Database("db_spotify")
    db.write(df, 'spotify')


def etl_process(filepath):
    data = extract(filepath)
    if data is None:
        print("Error: Unable to extract data from the file.")
        return
    data = transform(data)
    load(data)
