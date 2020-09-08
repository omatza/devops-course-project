# The purpose of memory game is to display an amount of random numbers to the users for 0.7 # seconds and then prompt
# them from the user for the numbers that he remember.
# If he was right with all the numbers the user will win otherwise he will lose.
#
# Example:
# User choose difficulty = 3
# 3 numbers between 1-101 will be generated to the user and will be shown in console for 0.7 seconds
# (using generate_sequence(difficulty)).
# User will enter the guessed numbers with an enter between each guess (using get_list_from_user(difficulty)).
# The list of the generated numbers and the list of the guessed numbers will be compared and will return true / false
# respectively

import random
import time
from Utils import screen_cleaner


def generate_sequence(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    C. The list will be shown for 0.7 seconds (using Utils.py module).
    :returns list generated
    """
    l = []
    for i in range(difficulty):
        l.append(random.randint(1, 101))

    return l


def get_list_from_user(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will prompt the user the following message:
    After seeing the numbers enter the numbers you saw, each one separated with Enter.
    C. Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    """
    l = []
    for i in range(difficulty):
        done = False
        while not done:
            inp = input("")
            if not inp.isdigit():
                print("numbers only")
                continue
            else:
                done = True
                l.append(int(inp))
    # print(l)
    return l


def is_list_equal(list_a, list_b):
    """
    A. Will get 2 variables named list_a and list_b
    B. The function will compare the two lists (list_a & list_b).
    C. The function will return True / False if the lists equal or not.
    :param list_a:
    :param list_b:
    :return:
    """
    list_a.sort()
    list_b.sort()
    for i in range(len(list_a)):
        if list_a[i] != list_b[i]:
            return False
    return True


def play(difficulty):
    """
    A. Will get a number variable named difficulty
    B. Will call the functions above and play the game.
    C. Will return True / False if the user lost or won (based on is_list_equal()).
    :param difficulty:
    :return: True / False if the user lost or won
    """
    print("===================== welcome to the memory game =====================")
    print("you need to remember a sequence of numbers that the computer will show")
    print("======================================================================")
    generated_list = generate_sequence(difficulty)
    print("After seeing the numbers, enter the numbers you saw, each one separated withEnter.")
    print(generated_list)
    time.sleep(0.7)
    screen_cleaner()
    user_list = get_list_from_user(difficulty)
    return is_list_equal(user_list, generated_list)
