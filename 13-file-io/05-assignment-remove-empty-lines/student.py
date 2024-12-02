def remove_empty_lines(source, destination):
    source_lines = []
    with open(source, encoding="utf-8") as source:
        source_lines = source.readlines()

    with open(destination, "w", encoding="utf-8") as destination:
        for line in source_lines:
            if len(line) > 1:
                destination.write(line)