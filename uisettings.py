import os
import time


# Available Rich colors
COLORS = [
    "black", "red", "green", "yellow",
    "blue", "magenta", "cyan", "white",
    "bright_black", "bright_red", "bright_green",
    "bright_yellow", "bright_blue", "bright_magenta",
    "bright_cyan", "bright_white",
]

# Available Rich styles
STYLES = [
    "bold",
    "dim",
    "italic",
    "underline",
    "blink",
    "reverse",
    "strike",
    "overline",
]


# Default theme settings
theme = {
    "prompt": "bold green",
    "path": "bold cyan",
    "command": "bold white",
    "output": "white",
    "muted": "dim white",
}

header = {
    "title": "bold green",
    "subtitle": "dim white",
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def get_color():
    while True:
        color = input("Enter color: ").strip().lower()
        parts = color.split()

        if not parts:
            print("Color cannot be empty!")
            continue

        color_name = parts[-1]
        styles = parts[:-1]

        if color_name not in COLORS:
            print("Invalid color!")
            continue

        if not all(style in STYLES for style in styles):
            print("Invalid style!")
            continue

        return color


def customize_theme():
    print("Let's start...")
    time.sleep(2)
    clear()

    print("=== Theme Colors ===\n")

    for key in theme:
        print(f"Customize {key}:")
        theme[key] = get_color()

    clear()

    print("=== Header Colors ===\n")

    for key in header:
        print(f"Customize {key}:")
        header[key] = get_color()

    print("\nSettings updated successfully!")
    time.sleep(2)
    clear()


def main():
    print("Change UI settings?")
    print("1. Yes")
    print("2. No")

    try:
        change = int(input("Choose: "))

        if change == 1:
            customize_theme()

        elif change == 2:
            print("Default settings selected.")

        else:
            print("Invalid option!")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()