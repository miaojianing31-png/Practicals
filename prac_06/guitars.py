"""
CP1404 Practical 06 - Guitars client program.
"""

from prac_06.guitar import Guitar


def main():
    """Get guitar details from the user and display all guitars."""
    guitars = []

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        print()

        name = input("Name: ")

    print()
    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""

        print(
            f"Guitar {i}: {guitar.name:>20} "
            f"({guitar.year}), worth "
            f"${guitar.cost:10,.2f}{vintage_string}"
        )


main()