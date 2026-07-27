"""
CP1404 Practical 06 - ProgrammingLanguage class.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a formatted description of the programming language."""
        return (
            f"{self.name}, {self.typing} Typing, "
            f"Reflection={self.reflection}, "
            f"First appeared in {self.year}"
        )

    def is_dynamic(self):
        """Return whether the programming language is dynamically typed."""
        return self.typing == "Dynamic"