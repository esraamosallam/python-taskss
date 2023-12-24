vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
string3 = 'samy'
result = ''
for i in string3:
    if i not in vowels:
        result = result + i
print(result)
