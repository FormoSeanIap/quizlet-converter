import sys
import os

def convert(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        file_base_name = os.path.splitext(file_name)[0]
        text = f.read()
        text_split = text.split("\n")
        with open(f"{file_base_name}-converted.txt", "w", encoding="utf-8") as output_file:
            for line in text_split:
                line_parts = line.split()
                line_new = f"{line_parts[0]}({line_parts[2]}),{line_parts[1]}"
                output_file.write(line_new + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <file_name>")
        sys.exit(1)
    else:
        convert(sys.argv[1])