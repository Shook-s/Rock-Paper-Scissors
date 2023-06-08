#Rock Paper Scissors
import time
import random
print("hi this is rock-paper-scissors by shook-s")
print("You can either choose to try and beat the computer or always loose to the computer")

while True:
    choose_mode = input("[1] Beat computer\n[2] Lose to computer\n")
    if choose_mode in ["1","2"]:
        break
    else:
        print("Choose either 1 or 2!")

list_of_choices_human = [["Rock","rock","1"],["Paper","paper","2"],["Scissors","scissors","3"]]

def play():
    choice = choosing()
    countdown(choice)
    showdown(choice)

if choose_mode == "1":
    play()
elif choose_mode =="2":
    print("You chose 2")

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



def countdown(choice):
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Shoot!")

    print(f"you:{choice}")
    print(f"computer:{comp_choice_random}")

list_of_choices_comp = ["Rock","Paper","Scissors"]
comp_choice_random = random.choice(list_of_choices_comp)

def showdown(choice):
    if choice == comp_choice_random:
        print("Tie!")
        play_again()
    elif choice == "Rock" and comp_choice_random == "Paper":
        print("You lose")
        play_again()
    elif choice == "Rock" and comp_choice_random == "Scissors":
        print("You win!")
        play_again()
    elif choice == "Paper" and comp_choice_random == "Scissors":
        print("You lose")
        play_again()
    elif choice == "Paper" and comp_choice_random == "Rock":
        print("You win!")
        play_again()
    elif choice == "Scissors" and comp_choice_random == "Rock":
        print("You lose")
        play_again()
    elif choice == "Scissors" and comp_choice_random == "Paper":
        print("You win!")
        play_again()


def end():
    print("Bye bye I hope you enjoyed")
    print("Again my github is shook-s shoot me a message I would love some criticism")


def play_again():
    valid_choices = ["Y", "y", "N", "n"]
    while True:
        choose_to_play_again = input("Do you want to play again? [Y/N] ")
        if choose_to_play_again in valid_choices:
            break
        else:
            print("Choose either yes or no")
    if choose_to_play_again == "Y" or choose_to_play_again == "y":
        play()
    else:
        end()

