# getting total & average of some numbers
total = count = avg = 0
num = input("Please enter a number: ")
while num != 'done':
    if num.isdigit():
        num = int(num)
        total += num
        count +=1
        num = input("Please enter a number: ")
    else:
        num = input("Please enter a number: ")
avg = total//count
print(f'total is {total}')
print(f'count is {count}')
print(f'average is {avg}')
