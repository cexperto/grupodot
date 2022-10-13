def find_palindromes(word):
    palindromes = {}
    for i in range(len(word)):
        for j in range(i+1,len(word)+1):
            ranges = word[i:j]
            if ranges == ranges[::-1]:
                palindromes[ranges] = len(ranges)
    values_items = []
    for i in palindromes.values(): 
        values_items.append(i)    
    return list(palindromes.keys())[list(palindromes.values()).index(max(values_items))]