import random
import datetime

print("Hello,\nWelcome to Dice Rolling!!\n")
user=input("Do you want to play game [y/n]: ")
user = user.lower()
score=0

if user == "y":
    times=int(input("How many times you want to play the game: "))
    for i in range(1,times+1):
        rand=random.randint(1,6)
        score+=rand
        print(f"You score {rand} in {i} times!\n")
    print("Your total score: ",score)
        

elif user == "n":
    print("Your score is: ",score)

else:
    print("You entered a wrong input")
