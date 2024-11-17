def plagiarism(s1, s2):
    s1 = s1.replace("\n", " ")
    s1 = set(s1.split(" "))

    s2 = s2.replace("\n", " ")
    s2 = set(s2.split(" "))
    
    return len(s1.intersection(s2))
    

print(plagiarism("a\nb\nc", "x\ny\nz"))