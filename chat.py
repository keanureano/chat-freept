import os
import sys
import time
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

HOME_URL = "https://chat.openai.com"
LOGIN_URL = "https://chat.openai.com/auth/login"


class ChatFreePT:
    def __init__(self, headless=True, profile="Default"):
        self.headless = headless
        self.profile = profile
        self.driver = None
        self.open()

    def _initialize_driver(self, login_mode=False):
        if self.driver:
            self.driver.quit()

        options = webdriver.ChromeOptions()
        options.add_argument(
            f"--user-data-dir=C:/Users/{os.getlogin()}/AppData/Local/Google/Chrome/User Data/{self.profile}"
        )

        if self.headless and not login_mode:
            options.add_argument("--headless")

        self.driver = Chrome(options=options)
        self.driver.get(HOME_URL)

    def _send_prompt(self, prompt):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 60)
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'textarea[placeholder="Send a message"]')
            )
        )
        textarea = self.driver.find_element(
            By.CSS_SELECTOR, 'textarea[placeholder="Send a message"]'
        )
        textarea.send_keys(prompt, Keys.ENTER)

    def _await_response(self):
        time.sleep(2)

        def locate_latest_chat_element():
            chat_elements = self.driver.find_elements(By.CSS_SELECTOR, ".markdown")
            return chat_elements[-1]

        try:
            wait = WebDriverWait(self.driver, 60)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".markdown")))
            latest_chat_element = locate_latest_chat_element()
            wait.until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".result-streaming"))
            )
            return latest_chat_element.text
        except StaleElementReferenceException:
            latest_chat_element = locate_latest_chat_element()
            return latest_chat_element.text

    def close(self):
        self.driver.close()

    def chat(self, text):
        self._send_prompt(text.replace("\n", "; "))
        return self._await_response()

    def open(self):
        self._initialize_driver()

        if self.driver.current_url == LOGIN_URL:
            print(f"LOGIN REQUIRED: Please log in to ChatGPT.")
            self._initialize_driver(login_mode=True)
            input(f"Press enter after logging in...")
            self._initialize_driver()


if __name__ == "__main__":
    chatbot = ChatFreePT(headless=False)

    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    else:
        prompt = "Hello world!"

    print(f"[User]: {prompt}")
    print(f"Awaiting Response...")

    latest_response = chatbot.chat(prompt)
    print(f"[Chat-FreePT]: {latest_response}")

    chatbot.close()
    exit
