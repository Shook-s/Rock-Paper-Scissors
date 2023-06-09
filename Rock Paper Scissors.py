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

play_count_normal = 0
play_count_auto_win = 0
play_count_auto_lose = 0

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


def showdown(choice):

    list_of_choices_comp = ["Rock","Paper","Scissors"]
    comp_choice_random = random.choice(list_of_choices_comp)

    outcomes = {
        "Rock": {"Scissors": "You win!", "Paper": "You lose"},
        "Paper": {"Rock": "You win!", "Scissors": "You lose"},
        "Scissors": {"Paper": "You win!", "Rock": "You lose"}
    }

    if choose_mode == "1":


        if choice == comp_choice_random:
            print(f"you:{choice}")
            print(f"computer:{comp_choice_random}")
            print("Tie!")
            play_again()
        else:
            result = outcomes.get(choice)
            if result:
                if comp_choice_random in result:
                    print(f"you:{choice}")
                    print(f"computer:{comp_choice_random}")
                    print(result[comp_choice_random])
                    play_again()

    elif choose_mode == "3":
        if choice == "Rock":
            comp_forced_choice = "Scissors"
        elif choice == "Paper":
            comp_forced_choice = "Rock"
        elif choice == "Scissors":
            comp_forced_choice = "Paper"
        
        print(f"you:{choice}")
        print(f"computer:{comp_forced_choice}")
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

    play_again()


def end():
    print("Bye bye I hope you enjoyed")
    print("Again my github is shook-s shoot me a message I would love some criticism")


def play_again():
    while True:
        choose_to_play_again = input("Do you want to play again? [Y/N] ")
        if choose_to_play_again in ["Y", "y", "N", "n","1","2"]:
            break
        else:
            print("Choose either yes or no")
    if choose_to_play_again in ["Y","y","1"]:
        if choose_mode == "1":
            global play_count_normal
            play_count_normal += 1
            if play_count_normal > 4:
                print("huh you really are a passionate player")
            play()

        elif choose_mode =="2":
            global play_count_auto_lose
            play_count_auto_lose += 1
            if play_count_auto_lose > 4:
                print("you're still at it?")
            comp_play()

        elif choose_mode == "3":
            global play_count_auto_win
            play_count_auto_win += 1
            if play_count_auto_win > 4:
                print("You really like the taste of victory don't you")
            play()
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

if choose_mode == "1" or choose_mode =="3":
    play()
elif choose_mode == "2":
    comp_play()
