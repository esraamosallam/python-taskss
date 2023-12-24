# email and username check
name = input("Please enter your name: ")
while True:
    if name.isdigit() or name == '' or name == ' ':
        name = input("Please enter a valid name: ")
    else:
        email = input("Please enter your E-mail: ")
        while '@gmail.com' not in email:
            print("Invalid E-mail!!")
            email = input("Please enter your E-mail: ")
    print('Good')
    break
