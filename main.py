from db import Database
from etl import etl_process

from business import *


def main():
    # Specify the path to your data file here.
    filepath = "spotify.csv"

    # Run the ETL process
    etl_process(filepath)

    # specify the name of your database
    db_name = 'db_spotify'
    # load the data from the database
    db = Database(db_name)
    df = db.read('spotify')

    albums_per_year(df)


if __name__ == "__main__":
    main()