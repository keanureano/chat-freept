import os
import sys
import time
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

HOME_URL = "https://chat.openai.com"
LOGIN_URL = "https://chat.openai.com/auth/login"


class ChatFreePT:
    def __init__(self, headless=True, profile="Default"):
        self.headless = headless
        self.profile = profile
        self.driver = None

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
        time.sleep(1)
        textarea = self.driver.find_element(
            By.CSS_SELECTOR, 'textarea[placeholder="Send a message"]'
        )
        textarea.send_keys(prompt, Keys.ENTER)

    def _await_response(self):
        time.sleep(3)
        WAIT_DURATION = 60

        response = self.driver.find_element(
            By.CSS_SELECTOR,
            ".markdown",
        )
        WebDriverWait(self.driver, WAIT_DURATION).until_not(
            lambda driver: "result-streaming" in response.get_attribute("class")
        )
        return response.text

    def close(self):
        self.driver.close()

    def chat(self, text):
        self._send_prompt(text)
        return self._await_response()

    def open(self):
        self._initialize_driver()

        if self.driver.current_url == LOGIN_URL:
            print(f"{Fore.RED}LOGIN REQUIRED: Please log in to ChatGPT. {Fore.RESET}")
            self._initialize_driver(login_mode=True)
            input(f"{Fore.RED}Press enter after logging in... {Fore.RESET}")
            self._initialize_driver()


if __name__ == "__main__":
    chatbot = ChatFreePT(headless=False)
    chatbot.open()

    if len(sys.argv) > 1:
        prompt = sys.argv[1].replace("\n", "; ")
    else:
        prompt = "Hello world!"

    print(f"{Fore.LIGHTBLUE_EX}[User]: {prompt}{Fore.RESET}")
    print(f"{Fore.LIGHTBLACK_EX}Awaiting Response...{Fore.RESET}")

    response = chatbot.chat(prompt)
    print(f"{Fore.GREEN}[Chat-FreePT]: {response}{Fore.RESET}")

    chatbot.close()
    exit
