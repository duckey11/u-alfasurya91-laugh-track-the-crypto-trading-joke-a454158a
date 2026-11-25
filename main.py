import os

JOKE = "Budi refreshed his portfolio 214 times today, finally saw green after three months, and screenshot it to the group chat before noticing the green was just his phone battery icon at 100%."

def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
