"""
CP1404 Practical 05 - Emails
"""


def main():
    """Store emails and associated names."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ("", "y"):
            name = input("Name: ").strip()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from an email address."""
    email_name = email.split("@")[0]
    name_parts = email_name.split(".")
    return " ".join(name_parts).title()


main()