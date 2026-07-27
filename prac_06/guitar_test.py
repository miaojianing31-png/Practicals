"""
CP1404 Practical 06 - Test the Guitar class.

"""

from datetime import datetime

from prac_06.guitar import Guitar


def main():
    """Test the Guitar class methods."""
    current_year = datetime.now().year

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000)
    boundary_guitar = Guitar(
        "50-year-old guitar", current_year - 50, 500
    )

    expected_gibson_age = current_year - 1922
    expected_another_age = current_year - 2013

    print(
        f"{gibson.name} get_age() - "
        f"Expected {expected_gibson_age}. "
        f"Got {gibson.get_age()}"
    )

    print(
        f"{another_guitar.name} get_age() - "
        f"Expected {expected_another_age}. "
        f"Got {another_guitar.get_age()}"
    )

    print(
        f"{gibson.name} is_vintage() - "
        f"Expected True. Got {gibson.is_vintage()}"
    )

    print(
        f"{another_guitar.name} is_vintage() - "
        f"Expected False. Got {another_guitar.is_vintage()}"
    )

    print(
        f"{boundary_guitar.name} is_vintage() - "
        f"Expected True. Got {boundary_guitar.is_vintage()}"
    )


main()