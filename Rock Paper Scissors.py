#Rock Paper Scissors
import time
import random
print("hi this is rock-paper-scissors by shook-s")
print("You can either choose to try and beat the computer, always loose to the computer or always win")


while True:
    choose_mode = input("[1] Beat computer\n[2] Lose to computer\n[3] Always win agaisnt computer\n")
    if choose_mode in ["1","2","3"]:
        break
    else:
        print("Choose either 1, 2 or 3!")


def choosing():
    while True:
        choice = input("Choose either rock, paper, or scissors: ")
        valid_choice = False

        for sub_list in [["Rock","rock","1"],["Paper","paper","2"],["Scissors","scissors","3"]]:
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


def countdown():
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Shoot!")

list_of_choices_comp = ["Rock","Paper","Scissors"]
comp_choice_random = random.choice(list_of_choices_comp)

def showdown(choice):

    print(f"you:{choice}")
    print(f"computer:{comp_choice_random}")

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

def comp_showdown(choice):
    
    if choice == "Scissors":
        comp_choice = "Rock"
    elif choice == "Rock":
        comp_choice = "Paper"
    elif choice == "Paper":
        comp_choice = "Scissors"

    if choose_mode == "2":    
        print(f"you:{choice}")
        print(f"computer:{comp_choice}")
        print("You lose!")
    elif choose_mode == "3":
        print(f"you:{comp_choice}")
        print(f"computer:{choice}")
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
        if choose_mode == "1":
            play()
        else:
            comp_play()
    else:
        end()


def play():
    choice = choosing()
    countdown()
    showdown(choice)

def comp_play():
    choice = choosing()
    countdown()
    comp_showdown(choice)

if choose_mode == "1":
    play()
elif choose_mode == "2" or choose_mode =="3":
    comp_play()

# For future I want to add a tracker for play count