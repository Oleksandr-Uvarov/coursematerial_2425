def spellcheck(document, valid_words):
    if len(document) == 0:
        return set('')
    
    document_lower = document.lower()


    document_lower = document_lower.replace('\n', ' ')
    words = document_lower.split(" ")
    
    word_set = set()

    for word in words:
        if word not in valid_words:
            word_set.add(word)

    return word_set


print(spellcheck("the cat\nsat on\nthe mat", ['cat', 'sat', 'mat']))