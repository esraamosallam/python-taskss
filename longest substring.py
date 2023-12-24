# longest substring of alphabetical order
def alphaFunc(string:str):
    longstring =string[0]   
    genstring =string[0]                 
    for i in string[1:] :
        if i > genstring[-1]:
            genstring += i
            if len(genstring)>len(longstring): 
                longstring=genstring
        else:
            genstring = i
    return longstring

longest_substring=alphaFunc('abdulrahman')
print(longest_substring)
