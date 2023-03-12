import sys
import os

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

def split_lines(text):
    return text.split("\n")

def convert_line(line):
    line_parts = line.split()
    if len(line_parts) == 2:
        # no reading. e.g. マスコミ    大眾傳媒、媒體、傳媒業 -> (大眾傳媒、媒體、傳媒業),マスコミ
        writing = line_parts[0]
        meaning = line_parts[-1]
        line_new = f"({meaning}),{writing}"
    else:
        # has reading. e.g. 落價 lo̍h-kè	降價 -> lo̍h-kè(降價),落價
        # has reading with multiple parts. e.g. 兩蕊目睭 nn̄g lúi ba̍k-chiu	兩隻眼睛 -> nn̄g lúi ba̍k-chiu(兩隻眼睛),兩蕊目睭
        writing = line_parts[0]
        reading = ""
        for i in range(1, len(line_parts) - 1):
            reading += f'{line_parts[i]} '
        meaning = line_parts[-1]
        line_new = f"{writing}({meaning}),{reading}"
    return line_new

def write_output(output_file_name, text):
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        for line in text:
            line_new = convert_line(line)
            output_file.write(line_new + "\n")

def convert(file_name):
    file_base_name = os.path.splitext(file_name)[0]
    text = read_file(file_name)
    text_split = split_lines(text)
    output_file_name = f"{file_base_name}-converted.txt"
    write_output(output_file_name, text_split)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py <file_name>")
        sys.exit(1)
    else:
        convert(sys.argv[1])