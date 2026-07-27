"""
CP1404 Practical 06 - Guitar class.
"""

from datetime import datetime


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted description of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the guitar's age in years."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return whether the guitar is at least 50 years old."""
        return self.get_age() >= 50