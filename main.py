from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

SIMILAR_ACCOUNT = "account"
ACCOUNT_NAME = "your_account_name"
ACCOUNT_PASSWORD = "your_password"


class InstaFollower:
    def __init__(self):
        s = Service("../../Coding/Chrome Driver/chromedriver.exe")

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(service=s, options=options)
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(60)

    def login(self):
        username_input = self.driver.find_element(By.NAME, "username")
        for letter in ACCOUNT_NAME:
            username_input.send_keys(letter)
            time.sleep(0.2)

        password_input = self.driver.find_element(By.NAME, "password")
        for letter in ACCOUNT_PASSWORD:
            password_input.send_keys(letter)
            time.sleep(0.2)

        enter_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        enter_button.click()

    def find_followers(self):
        search_bar = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        for letter in SIMILAR_ACCOUNT:
            search_bar.send_keys(letter)
            time.sleep(0.2)

        found_account_bar = self.driver.find_element(By.CSS_SELECTOR, "._01UL2 .fuqBx a")
        found_account_bar.click()

        followers_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/'
                                                              'div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(2)

    def follow(self):
        modal = self.driver.find_element(By.CLASS_NAME, "isgrP")
        for _ in range(10):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".PZuss button")
        for button in follow_buttons:
            if button.text == "Followers" or button.text == "Request sent":
                pass
            else:
                time.sleep(2)
                button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
