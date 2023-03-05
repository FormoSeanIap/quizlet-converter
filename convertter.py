with open("test.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text_split = text.split("\n")
    for line in text_split:
        line_parts = line.split()
        line_new = f"{line_parts[0]}({line_parts[2]}),{line_parts[1]}"
        print(line_new)
