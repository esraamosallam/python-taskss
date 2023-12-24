# reversing string
def stringFunc(x : str):
    l2 = []
    l1 = list(x)
    for i in l1:
        l2.append(i)
    l2.reverse()
    a = ''.join(l2)
    print(a)

stringFunc('zahra')

#________________________________
def stringFunc(x : str):
    return x[::-1]

s = stringFunc('zahra')
print(s)
