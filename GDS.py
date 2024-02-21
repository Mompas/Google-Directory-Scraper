from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import re
import os
from bs4 import BeautifulSoup
import pyautogui


def print_lollipop():
    print("")
    print("")
    print("")
    print("")
    print("\033[94m====================== Created By Mompas =====================\033[0m")
    print("")
    print("")
    print("\033[38;5;205m                           (~~~~~~~~)    ")
    print("                          (~~~~~~~~~~)   ")
    print("                         (~~~~~~~~~~~~)  \033[0m")
    print("\033[95m                        (*############*) ")
    print("                        (*############*) \033[0m")
    print("\033[38;5;205m                         (~~~~~~~~~~~~)  ")
    print("                          (~~~~~~~~~~)   ")
    print("                           (~~~~~~~~)    \033[0m")
    print("                               ||      ")
    print("                               ||      ")
    print("                               ||      ")
    print("                               ||      ")
    print("")
    print("\033[94m================== https://github.com/Mompas ==================\033[0m")
    print("\033[91m")
    print("          !!! NOT INTENDED FOR MALICIOUS ACTIVITY !!!")
    print("")
    print("\033[0m")
    print("")
    print("")
    print("")
    print("")

def login_and_extract_emails(username, password, login_url, target_url):
        chrome_service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=chrome_service)

        # First page: Submit username
        driver.get(login_url)
        username_input = driver.find_element(By.ID, 'identifierId')
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)

        # Wait for the second page to load
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))

        # Second page: Submit password
        password_input = driver.find_element(By.NAME, 'Passwd')
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        # Wait for the target URL to load
        time.sleep(2)
        WebDriverWait(driver, 3)
        driver.get(target_url)
        # Extract email addresses from the visible content
        wait = WebDriverWait(driver, 10)
        target_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.W7Nbnf')))

########################## MODIFY THIS PART FOR DIFFERENT USE CASES ##########################

        x_coordinate = 1000
        y_coordinate = 250
        time.sleep(2)
        pyautogui.moveTo(x_coordinate, y_coordinate)
        pyautogui.click()
        time.sleep(2)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(4)


        with open(output, 'w') as file:
            for _ in range(50):
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
                time.sleep(0.5)
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'html.parser')
                email_elements = soup.find_all('div', {'class': 'W7Nbnf'})
                email_addresses = [element.text for element in email_elements if element.text.endswith('.com')]
                file.write('\n'.join(email_addresses))
                print('\n'.join(email_addresses))

################################################################################################


print_lollipop()
# If you want a permenant option, uncomment the two lines bellow and comment the input version.
# username = 'your-username'
# password = 'your-password'
username = input("Enter Your Gmail: ")
password = input("Enter Your Password: ")
print("Enter Your Chromedriver's Path")
user_path = input("Example: \\Users\\Smith\\Desktop\\chromedriver.exe" + '\n')
chromedriver_path = "C:\\" + user_path
user_output = input("Enter Output File Name (Without .txt): ")
output = user_output + ".txt"

login_url = 'https://accounts.google.com/'
target_url = 'https://contacts.google.com/directory'

login_and_extract_emails(username, password, login_url, target_url)