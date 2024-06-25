from etl import etl_process


def main():
    # Specify the path to your data file here.
    filepath = "spotify.csv"

    # Run the ETL process
    etl_process(filepath)


if __name__ == "__main__":
    main()