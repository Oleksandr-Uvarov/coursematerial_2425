def remove_duplicate_lines(source, destination):
    source_lines = []
    with open(source, encoding="utf-8") as source:
        source_lines = source.readlines()
        print(source_lines)

    with open(destination, "w", encoding="utf-8") as destination:
        
        for i in range(0, len(source_lines) - 1):
            if source_lines[i] != source_lines[i+1] or i == 0:
                destination.write(source_lines[i])



remove_duplicate_lines("input.txt", "output.txt")