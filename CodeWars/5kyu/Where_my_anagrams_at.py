def anagrams(word, words):
    l=[]
    for w in words:
        counter=0
        word_copy=list(word)
        for char in w:
            if char in word_copy:
                word_copy.remove(char)
                counter+=1
        if counter >= len(w) and counter >= len(word):
            l.append(w)
    return l