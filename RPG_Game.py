import time
from sys import exit


def gold_room():
    print("This is a room full of gold.How much do you want to take?")
    player_choice = input("> ")

    if "0" in player_choice or "1" in player_choice:
        how_much = int(player_choice)
    else:
        dead("Dude, This wont work!!")
    if how_much < 50:
        print("You're not greedy and you win!!")
        time.sleep(10)
        exit(0)
    else:
        dead("You're greedy.")


def bear_room():
    print("""
    There is a bear here.
    The bear has a bunch of honey.
    The Fat Bear is infront of the Door.
    How are you going to move the bear?
    """)
    bear_moved = False
    while True:
        choice_1 = input(">")
        choice = choice_1.lower()
        if choice == "take honey":
            dead("The Bear look at you and slaps your face off!!")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear moved!!!")
            print("You can go inside the room now!!")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is angry and he chops your legs!!")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            dead("You tried to outsmart the bear and youre dead!!")
        else:
            print("I have no idea what language youre speaking!!")


def dark_room():
    print("""
    Here you see the Great Evil Dark-sama.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head.
    """)
    choice_1 = input(">")
    choice = choice_1.lower()
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty.")
    else:
        dark_room()


def start():
    print("""
    There is a door on your right and left.
    You are in a dark room
    Which door do you take?
    """)
    choice_1 = input(">")
    choice = choice_1.lower()
    if choice == "left":
        bear_room()
    elif choice == "right":
        dark_room()
    else:
        dead("You stumble around the room you starve to death.")


def dead(ded_msg):
    print(ded_msg + "Good Job!!")
    time.sleep(10)
    exit(0)


start()
