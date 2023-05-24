# ----------------------------------------imports------------------
from time import sleep
import os
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ---------------------------constants-------------------------------
username = os.environ["name"]
password = os.environ["pass"]
similar_account = "433"
follow_count = 15


# ---------------------------driver-------------------------------
class InstaFollower:
    def __init__(self):
        self.search_button = None
        chrome_driver_path = Service(executable_path="C:/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_driver_path)

    def login(self):
        url = "https://www.instagram.com/"
        self.driver.get(url)
        sleep(20)
        username_entry = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_entry.send_keys(username)
        username_entry.send_keys(Keys.RETURN)
        sleep(2)
        password_entry = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_entry.send_keys(password)
        password_entry.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))).click()

        sleep(20)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")

        sleep(20)
        buttons = self.driver.find_elements(by=By.CSS_SELECTOR,
                                            value='._ac2a')
        followers_list = [button for button in buttons]
        followers_list[1].click()
        sleep(20)
        for _ in range(follow_count):
            scr1 = self.driver.find_element(by=By.CSS_SELECTOR, value='._aano')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        sleep(5)

    def follow(self):
        all_follow_button = self.driver.find_elements(by=By.CSS_SELECTOR,
                                                      value='._aacl _aaco _aacw _aad6 _aade')
        for follow_button in all_follow_button:
            try:
                follow_button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH,
                                                         value='//*[@id="mount_0_0_LC"]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel_button.click()

        sleep(20)
        self.driver.quit()
