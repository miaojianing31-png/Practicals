"""CP1404 Practical 05 - Hexadecimal colour lookup."""

NAME_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "aquamarine": "#7fffd4",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "coral": "#ff7f50",
    "darkgreen": "#006400",
    "gold": "#ffd700",
    "hotpink": "#ff69b4",
    "orange": "#ffa500",
    "white": "#ffffff"
}

colour_name = input("Enter colour name: ").strip().lower()

while colour_name != "":
    try:
        print(f"{colour_name.title()} is {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")

    colour_name = input("Enter colour name: ").strip().lower()

print("Finished.")