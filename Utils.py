# This file will contain general information and operations we need for our game.
# 1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
# 2. ERROR_MESSAGE: “Something went wrong..”
# 3. screen_cleaner - A function to clear the screen
#    (useful when playing memory game or before a new game starts).
#  * The following code can be used: os.system('cls' if os.name == 'nt' else 'clear') *
import os

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong.."


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def error_message(error_string):
    return ERROR_MESSAGE + "\n" + error_string
