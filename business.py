import matplotlib.pyplot as plt


def albums_per_year(data):
    # Suppose que l'année est le premier élément de chaque entrée de données
    frequency_dict = {}
    for entry in data:
        year = entry[0]
        if year is not None:
            if year not in frequency_dict:
                frequency_dict[year] = 1
            else:
                frequency_dict[year] += 1

    years = sorted(frequency_dict.keys())
    counts = [frequency_dict[year] for year in years]

    plt.plot(years, counts)
    plt.xlabel('Year')
    plt.ylabel('Number of Albums')
    plt.savefig('albums_per_year.png')