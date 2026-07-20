"""
CP1404 Practical 05 - Wimbledon
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Read and process Wimbledon data."""
    records = read_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    print(champion_to_wins)
    print(countries)

    """Read and display Wimbledon data."""
    records = read_data(FILENAME)
    print(records)


def read_data(filename):
    """Read Wimbledon CSV data."""
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

main()