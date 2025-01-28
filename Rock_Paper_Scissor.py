import random
item_list=["rock","paper","scissor"]
score=0

for i in range(int(input("Enter no of chance: "))):
    user=input("Choose anyone from Rock, Paper or Scissor: ")
    user=user.lower()
    comp=random.choice(item_list)
    print(f"User choose {user} & Computer choose {comp}")
    
    if user=="rock":
        if comp=="paper":
            print("Paper win.\n")
            score-=1
        elif comp=="rock":
            print("Tie.\n")
        elif comp=="scissor":
            print("Rock win.\n")
            score+=1
        else:
            raise ValueError("You choose a wrong input.\n")
            break

    elif user=="paper":
        if comp=="paper":
            print("Tie.\n")
        elif comp=="rock":
            print("Paper win.\n")
            score+=1
        elif comp=="scissor":
            print("Scissor win.\n")
            score-=1
        else:
            raise ValueError("You choose a wrong input.\n")
            break

    elif user=="scissor":
        if comp=="scissor":
            print("Tie.\n")
        elif comp=="rock":
            print("Rock win.\n")
            score-=1
        elif comp=="paper":
            print("Scissor win.\n")
            score+=1
        else:
            raise ValueError("You choose a wrong input.\n")
            break

    else:
        raise ValueError("You choose a wrong input.\n")
        break
print(f"The user Scored {score} points.")