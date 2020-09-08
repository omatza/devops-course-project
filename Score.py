# A file which will manage the scores file.
# The scores file at this point will consist of only a number.
# That number is the accumulation of the winnings of the user.
# Amount of points for winning a game is = 1 point per difficulty level (difficulty 3 = 3 points).
# Each time the user is winning a game, the points he won will be added to his current amount of point saved in a file.

from Utils import SCORES_FILE_NAME


def add_score(points):
    """
    A. The function’s input is a variable called points.
    B. The function will try to read the current score in the scores file, if it fails it will create a
    new one and will use it to save the current score.
    C. The function will print the user current score.
    """
    # note:
    # r +
    # for read / write without deleting the original content if file exists, otherwise raise exception
    # w +
    # for delete the original content then read / write if file exists, otherwise create the file
    # so I couldn't open the file in one time with r+, if it is not exist, cause it failed, and w+ it wiped off to 0 len
    try:
        file = open(SCORES_FILE_NAME, 'r+', encoding='UTF-8')
    except IOError as e:
        file = open(SCORES_FILE_NAME, 'w+', encoding='UTF-8')  # create if it doesn't exist
    finally:
        file.close()

    try:
        file = open(SCORES_FILE_NAME, 'r+', encoding='UTF-8')
        file.seek(0)
        cur_points = file.read()
        if cur_points == '':
            cur_points = '0'

        new_points = points + int(cur_points)
        file.seek(0)
        file.write(str(new_points))
        file.close()
        print("Your current score is:", new_points)
    except IOError as e:
        print("some file operation failed")
    except Exception as be:
        print(be)
    finally:
        pass


# inp = int(input("enter number"))
# add_score(inp)

