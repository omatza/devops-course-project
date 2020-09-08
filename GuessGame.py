# The purpose of guess game is to start a new game, cast a random number between 1 to a variable called difficulty.
import random


def generate_number(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will return a random number between 1 to difficulty.
    :param difficulty:
    :return: random number between 1 to difficulty.
    """
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will ask the user to guess a number between 1 to difficulty and return the number the user guessed.
    :param difficulty:
    :return: number the user guessed
    """
    return_value = None
    done = False
    while not done:
        inp = input("Please guess a number between 1 to " + str(difficulty) + " : ")
        if (not inp.isdigit()) or int(inp) < 1 or int(inp) > difficulty:
            print("please read carefully and try again")
        else:
            return_value = int(inp)
            done = True
    return return_value


def compare_results(difficulty, secret_number):
    """
    A. Will get 2 variables: number variable named difficulty number variable named secret_number
    B. Will compare the secret generated number to the one prompted by the get_guess_from_user.
    :param difficulty:
    :param secret_number:
    :return: true is same
    """
    return difficulty == secret_number


def play(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will call the functions above and play the game.
    C. Will return True / False if the user lost or won.
    :param difficulty:
    :return: True / False if the user lost or won
    """
    print("============== welcome to the guess game ==============")
    print("you need to guess which number the computer will choose")
    print("=======================================================")
    random_number = generate_number(difficulty)
    secret_number = get_guess_from_user(difficulty)
    result = compare_results(random_number, secret_number)
    return result
