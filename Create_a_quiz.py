# output
print("Welcome to the Python")

# input
playing = input("Do you want to play a game? (yes/no) ")
if playing.lower() == "yes":
    print("Lets play")
    score = 0
else:
    print("Thank you")

answer = input("What is RAM? ")
if answer.lower() == "random access memory":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer = input("What is CPU? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer = input("What is GPU? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer = input("What is PSU? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")


print("Your score is " + str(score) + " question answered correctly")
print("your score is " + str((score/4)*100) + "%")
