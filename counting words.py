# counting specific word
st2 = 'I went to the iti to improve my career itiis awsome'
z = st2.count('iti')
print(z)
#another solution
st = 'iti'
count = 0
string2 = 'I went to the iti to improve my career iti is awsome'
listiti = string2.split()
for i in listiti:
    if i == st:
        count +=1
print(count)
