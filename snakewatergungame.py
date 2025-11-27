import random

computer = random.choice([-1,0,1])
yous = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

# check for invalid input
if yous not in youDict:
    print("Invalid input! Please enter s, w, or g only.")
    exit()

you = youDict[yous]

print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# game logic
if computer == you:
    print("It's a draw!")
elif (computer == -1 and you == 1) or \
     (computer == 1 and you == 0) or \
     (computer == 0 and you == -1):
    print("You win!")
else:
    print("You lose!")
