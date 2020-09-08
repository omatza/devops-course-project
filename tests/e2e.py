# this file is for testing the scores
# we will run it as selenium test
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_scores_service(app_url):
    """
    Method to test our web service.
    It gets the application URL as an input, open a browser to that URL, select the score element in our web page,
    check that it is a number between 0 to 1000 and return a boolean value if it’s true or not.
2. main_
    :param app_url: the url of the application
    :return: true if our score is between 0 to 1000. false otherwise
    """
    value = 1001
    driver = webdriver.Chrome(executable_path="C:\\Utils\\ChromeDriver.exe") #TODO: what about this hard coded path ?
    driver.implicitly_wait(10)  # set timeout to 10 seconds (instead of the default 0)

    driver.get(app_url)
    element = driver.find_element_by_id("score") #TODO: add try catch on this element
    value = int(element.text)
    driver.close()  # close the tab
    driver.quit()

    if 0 <= value and value <= 1000:
        return True
    else:
        return False


def main_function():
    """
    calls the test_scores_service
    :return: exit code -1 if test failed. 0 if passed.
    """
    #get the address from user as argument somehow ?
    #main_function("localhost:8777")

    if not test_scores_service("192.168.99.100:8777"):  #TODO: add dynamic addrress
        return -1

    return 0


if __name__ == '__main__':
    main_function()