# creating a list from 1 to 10
def funcOne(length, start):
    myList = []
    for i in range(start, length+start, 1):
        myList.append(i)
    print(myList)

funcOne(10,1)
