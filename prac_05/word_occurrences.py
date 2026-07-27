"""
CP1404 Practical 05 - Wimbledon
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Read, process and display Wimbledon data."""
    records = read_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def read_data(filename):
    """Read Wimbledon CSV data and return a list of records."""
    records = []

    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        for row in reader:
            records.append(row)

    return records


def process_data(records):
    """Create champion win counts and champion countries."""
    champion_to_wins = {}
    countries = set()

    for record in records:
        country = record[1]
        champion = record[2]

        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
        countries.add(country)

    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display Wimbledon champions and countries."""
    print("Wimbledon Champions:")

    for champion, number_of_wins in champion_to_wins.items():
        print(f"{champion} {number_of_wins}")

    sorted_countries = sorted(countries)

    print()
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()