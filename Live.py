import MemoryGame
import GuessGame
from Utils import error_message
from Score import add_score


def welcome(name):
    """
    This function gets a person name as an input and returns a string in the following layout:
    Hello <name> and welcome to the World of Games (WoG).
    Here you can find many cool games to play.
    :param name: name - the player's name
    """
    if type(name) != str:
        print("please enter a valid name")

    print("Hello", name, "and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")


def load_game():
    """
    This function:
    1. Will print out the following text:
    Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
    2. Will get an input from the user about the game he chose – 1/2.
    3. After receiving the game number from the user, the function will get the level of difficulty with
    the following text and also save to a variable:
    Please choose game difficulty from 1 to 5:
    4. Will start a new function of the corresponding game with the given difficulty.
    The function will check the input of the chosen game (the input supposed to be a number
    between 1 to 2), also will check the input of level of difficulty (input should be a number between
    1 to 5).
    In case of an invalid choice, return the ERROR_MESSAGE (Utils.py).
    For example: If a user will choose the first option in load_game() function with difficulty 3, it will
    call the play() function from the module MemoryGame with difficulty of 3.
    In case the user won the game, the function will call the function called add_score() (in score.py
    module) to add the new score the user won to the score saved in the Scores.txt function.
    In case the user lost, call load_game() again.
    """

    #  print menu to choose game from
    print("Please choose a game to play: (1 or 2)")
    print("\t1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("\t2. Guess Game - guess a number and see if you chose like the computer)")
    game = None
    difficulty = None
    while True:
        inp = input("Enter number between 1 - 2. X to exit ")
        if inp == "x":
            exit(0)
        try:
            int(inp)
        except ValueError:
            print(inp + " is not inp.isdigit()")
            continue
        if check_input_in_range(int(inp), 1, 2):
            break
    game = int(inp)

    while True:
        inp = input("Please choose game difficulty from 1 to 5: ")
        try:
            int(inp)
        except ValueError:
            print(inp + " is not inp.isdigit()")
            continue
        if check_input_in_range(int(inp), 1, 5):
            break
    difficulty = int(inp)

    # run the game
    result = None
    if game == 1:
        result = MemoryGame.play(difficulty)
    elif game == 2:
        result = GuessGame.play(difficulty)
    else:
        pass  # can't reach here

    # if user won add score and return. Else force the user to get better
    if result:
        print("Congratulations. You won :-)\n")
        add_score(difficulty)
    else:
        print("You lost. Maybe next time. Try again\n")
        load_game()


def check_input_in_range(inp, low, high):
    if (inp < low) or (inp > high):
        print(error_message("value is not in range [" + str(low) + "," + str(high) + "]"))
        return False
    return True

