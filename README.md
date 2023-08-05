# Chat-FreePT

Chat-FreePT is a Free API alternative that allows you to interact with OpenAI's ChatGPT in real-time. It uses Selenium and undetected-chromedriver to simulate a web browser, enabling you to have a conversation with ChatGPT just like you would on the OpenAI platform. This tool provides a simple interface for sending prompts to ChatGPT and receiving its responses instantly.

Please note that ChatFreePT is intended for educational purposes only. It is not an official API provided by OpenAI, and it should not be used for any commercial or production purposes. Use it responsibly and in compliance with OpenAI's usage policies.

## Requirements

- Python 3.6 or higher
- Chrome Browser installed
- ChromeDriver

## Setup

Before using Chat-FreePT, you need to download the Chrome browser and ChromeDriver. Follow the steps below:

1. Download Chrome and ChromeDriver Browser from the official website: [https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable).

2. Add the downloaded ChromeDriver executable to your system's PATH variable. This step is necessary to ensure that Selenium can locate the ChromeDriver when running the script.

Once you have completed the above setup, proceed with the following steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ChatFreePT.git
   cd ChatFreePT
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The `ChatFreePT` class in the `chat.py` script provides a way to interact with OpenAI's ChatGPT through the Chrome WebDriver. It utilizes Selenium and the undetected-chromedriver package to communicate with the browser.

To use the script, follow these steps:

1. Instantiate the `ChatFreePT` class:

   ```python
   chatbot = ChatFreePT()
   ```

2. Run the `open` method to set up the browser:

   ```python
   chatbot.open()
   ```

3. Provide a prompt for ChatGPT. You can either pass the prompt as an argument when running the script or use the default prompt "Hello world!" if no argument is provided.

4. Use the `chat` method to send the prompt and receive a response from ChatGPT:

   ```python
   response = chatbot.chat("Your prompt goes here")
   print(response)
   ```

5. After you are done with the conversation, close the browser:

   ```python
   chatbot.close()
   ```

## Script Options

- `headless`: If set to `True`, the script runs the browser in headless mode (no visible browser window). If set to `False`, it shows the browser window.
- `profile`: Sets the Chrome user profile to be used during interaction with ChatGPT.

## Examples

1. Basic usage with a custom prompt:

   ```python
   chatbot = ChatFreePT()
   chatbot.open()
   response = chatbot.chat("Tell me a joke")
   print(response)
   chatbot.close()
   ```

2. Running the script from the command line:

   ```bash
   python chat.py "Tell me a joke"
   [User]: Tell me a joke
   Awaiting Response...
   [Chat-FreePT]: Why did the chicken cross the road? To get to the other side!
   ```

## Important Notes

- The script waits for responses for a maximum of 60 seconds. If ChatGPT takes longer to respond, the script may terminate prematurely.
- The script is intended for personal use and may require updates if there are changes to the ChatGPT website structure.
