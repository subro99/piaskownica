def regex_contains_all(st): 
    # your code here
    reg=""
    for char in st:
        reg= reg + "(?=.*"+char+")"
        
        
    return reg