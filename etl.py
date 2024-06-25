from datetime import datetime

from dal import insert


def extract(filepath):
    # Extract data with specific columns
    data = []
    try:
        with open(filepath, encoding='latin1') as csv:
            lines = csv.readlines()
            for line in lines[1:]:
                list_fields = line.strip('\n').split(',')
                data.append(tuple(list_fields[1:29]))
        return data
    except Exception as e:
        print(e)


def transform(data):
    transformed_data = []
    for row in data:
        # extract year from 'Release Date'
        release_date = row[3]
        # try date formats
        try:
            year = datetime.strptime(release_date, "%m/%d/%Y").year
        except ValueError:
            try:
                year = datetime.strptime(release_date, "%M/%d/%Y").year
            except ValueError:
                try:
                    year = datetime.strptime(release_date, "%m/%d/%y").year
                except ValueError:
                    print(f"Unexpected date format in row {row}")
                    continue

        # convert 'TikTok Likes' to integer
        tiktok_likes = int(row[14])

        # append transformed row to transformed_data
        transformed_data.append((year, tiktok_likes) + tuple(row[:3]) + tuple(row[4:]))
    return transformed_data


def load(transformed_data):
    # Insert transformed_data into the database
    insert(transformed_data)


def etl_process(filepath):
    data = extract(filepath)
    if data is None:
        print("Error: Unable to extract data from the file.")
        return
    data = transform(data)
    load(data)
