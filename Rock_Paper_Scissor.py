"""
Workflow of Game:
1- Input from user(Rock/paper/Scissor)
2- Computer Choice(Random Option Chosen by Computer)
3- Result Print

Cases:
A - Rock
Rock- Rock    = Tie
Rock- Paper   = Paper Win
Rock- Scissor = Rock Win

B- Paper
Paper- Paper   = Tie
Paper- Rock    = Paper Win
Paper- Scissor = Scissor Win

C- Scissor
Scissor- Scissor = Tie
Scissor- Rock    = Rock Win
Scissor- Paper   = Scissor Win

"""

import random
item_list=["Rock","Paper","Scissor"]
user_Choice= input("Enter your move (Rock/Paper,Scissor) = ").capitalize()
comp_Choice= random.choice(item_list)
print(f"User Choice= {user_Choice}, Computer Choice= {comp_Choice}")

if user_Choice ==comp_Choice:
    print("Both Cases Same: Match Tie!!!")
elif user_Choice=="Rock":
    if comp_Choice=="Paper":
        print("Paper Covers Rock. Hence, Paper Wins!!!")
    else:
        print("Rock Smashes Scissor. Hence, You Wins!!!")

elif user_Choice=="Paper":
    if comp_Choice=="Rock":
        print("Paper Covers Rock,Paper Wins!!!")
    else:
        print("Scissor cut Paper,Scissor Wins!!!")

elif user_Choice=="Scissor":
    if comp_Choice=="Rock":
        print("Rock Smashes Scissor, Rock Wins!!!")
    else:
        print("Scissor cut Paper, Scissor Wins!!!")
     