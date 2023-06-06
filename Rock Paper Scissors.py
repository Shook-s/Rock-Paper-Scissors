#Rock Paper Scissors
import time
import random
print("hi this is rock-paper-scissors by shook-s\ntry to beat the computer")
choices_dict = {
    "Rock":"1",
    "Paper":"2",
    "Scissors":"3"
}
list_of_choices_human = [["Rock","rock","1"],["Paper","paper","2"],["Scissors","scissors","3"]]

def choosing():
    while True:
        choice = input("Choose either rock, paper, or scissors: ")
        valid_choice = False

        for sub_list in list_of_choices_human:
            if choice in sub_list:
                valid_choice = True
                break

        if valid_choice:
            break
        else:
            print("You didn't chose rock paper or scissors!")

    if choice == "1" or choice == "rock":
        choice = "Rock"
    elif choice == "2" or choice == "paper":
        choice = "Paper"
    elif choice == "3" or choice == "scissors":
        choice = "Scissors"
    
    return choice


choice = choosing()

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("Shoot!")

list_of_choices_comp = ["Rock","Paper","Scissors"]
comp_choice_random = random.choice(list_of_choices_comp)

print(f"you:{choice}")
print(f"computer:{comp_choice_random}")

if choice == comp_choice_random:
    print("Tie! Try again")
    choosing()
elif choice == "Rock" and comp_choice_random == "Paper":
    pass