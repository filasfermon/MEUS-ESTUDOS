import random

print("There is a treasure you can find, but you need to pick the right path to it.")
print("In front of you thre are two roads to take. On on your wirte and one on your left. Choose one of them!")

move_1 = input("Type right or left to choosea path: \n")

radom_number = random.randint(1, 10)

if radom_number % 2 == 0 and move_1.lower() == "right":
    print("Good choice! Now, focus on the next move!")
    move_2 = input("Now you have two abandoned houses in front of you. One one your right and one on your left." 
                   "Choose one of them!"
                   "Type right or left: \n")
    if radom_number % 2 != 0 and move_2.lower() == "right":
        print("You are on the right path! Now, focus on the next move!")
        move_3 = input("Now you have two paths in front of you. One one your right and one on your left." 
                       "Choose one of them!"
                       "Type right or left: \n")
        if radom_number % 2 == 0 and move_3.lower() == "right":
            print("Congratulations! You found the treasure!")
        else:
            print("You are lost! Try again!")
    else:
        print("You are lost! Try again!")
else:
    print("Today is not your lucky day! try another time!")
