import random

print("GUESS THE NUMBER")
# i: Personal habit: set all necessary value(text, number etc.) first.
correctMessage = 'You are correct !'
incorrectMessage = 'You are wrong !'
endMessage = "Game Over, Thanks for playing"
# 1. System need to generate a random number first.
systemNum = float('{:.2f}'.format(random.random()))

# 2. Exception Handling and check user input.
try:
    # 2.1 ask for user input and format into 2 d.p.
    userNum = float(input("Please enter a number?: "))

    # 2.2 print out the basic information.
    print("System number is:", systemNum)
    print("Your number is", str(userNum))

    # 2.3 Compare the user and system values and return the message accordingly.
    if userNum == systemNum:
        print(correctMessage)
    else:
        print(incorrectMessage)
except:
    # 2.4 Handle exception case for user input
    print("Invalid Input, Pleas enter a correct value")
finally:
    # 3 Program ends and display end message
    print(endMessage)
