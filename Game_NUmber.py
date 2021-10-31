import random
def enterNumber():
    userNumber = int(input("Enter number : "))
    return userNumber

def compare(com):
    while True:
        num = enterNumber()
        if num > com:
            print("The number is over than ....")
            print("----------------------------")
        elif num < com:
            print("The number is less than ....")
            print("----------------------------")
        else:
            print("----------------------------")
            print("%d is Correct!!" %(com))
            break

resultNumber = random.randint(0, 100)
compare(resultNumber)
