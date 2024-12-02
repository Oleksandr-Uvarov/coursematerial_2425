def count_lines_in_file(file):
    with open(file, encoding="utf-8") as file:
        lines = file.readlines()
        return len(lines)