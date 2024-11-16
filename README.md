# StresserTelegram 🚀

A Python-based stress testing tool that interacts with Telegram bots. This project allows users to send a large number of requests to a specified Telegram bot to test its resilience and performance under high load.

## Table of Contents 📑

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Flood Wait Handling](#flood-wait-handling)
- [Notes on Usage](#notes-on-usage)
- [License](#license) 

## Introduction 📝

StresserTelegram is a tool designed to help you evaluate how a Telegram bot handles a significant load of incoming requests. The script uses the `telethon` library to communicate with Telegram, enabling it to send multiple messages to a specific bot username. The tool can be useful for performance testing, debugging, and optimizing bot infrastructure.

**Disclaimer**: ⚠️ This tool is meant solely for testing bots you own or have permission to test. Misuse of this tool against bots without proper authorization may lead to legal issues and violate Telegram's terms of service.

## Features ✨

- Allows the user to specify the bot to target via username.
- Adjustable number of requests to be sent.
- Handles `FloodWaitError` to prevent violating Telegram's rate limits.
- Generates "broken" random strings to simulate non-standard user input.

## Installation 🛠️

To use StresserTelegram, you need Python 3.7+ and the following dependencies installed:

1. Clone the repository:
   ```bash
   git clone https://github.com/CyberScopeToday/stressertelegram.git
   cd stressertelegram
   ```

2. Install the required Python packages:
   ```bash
   pip install telethon
   ```

## Usage 🚀

Before using the tool, you need to set up a Telegram API ID and hash, which you can get from [my.telegram.org](https://my.telegram.org).

Run the script using the command line:

```bash
python bot.py
```

Upon running the script, you will be prompted for:

- **Bot username** 🤖: Enter the Telegram username of the bot to which you want to send the requests (e.g., `@yourbotname`).
- **Number of requests** 🔢: Specify the number of requests/messages you want to send.

## Configuration ⚙️

### API Credentials 🔑

Update the following values in `bot.py` with your credentials:

- `api_id`: Your Telegram API ID.
- `api_hash`: Your Telegram API hash.
- `phone_number`: Your phone number to authenticate with Telegram.

```python
# Example configuration
api_id = 1234567
api_hash = 'your_api_hash_here'
phone_number = '+1234567890'
```

### Generating Broken Strings 🔀

The script generates random strings consisting of alphanumeric characters, punctuation, and whitespace to simulate non-standard user inputs.

## Flood Wait Handling ⏳

If Telegram detects rapid consecutive messages, it may enforce a "flood wait" restriction. In this case, the script will automatically handle the `FloodWaitError` by pausing for the required time (as indicated by the error message). This ensures that you do not violate Telegram's rate limits and avoid temporary bans.

## Notes on Usage 📌

- **Use Responsibly** ⚠️: Only use this tool on bots that you own or manage. Unauthorized testing is strictly forbidden.
- **Rate Limits** ⏱️: Telegram imposes rate limits on how many messages can be sent within a specific time frame. The tool incorporates a delay to avoid these limits, but it is not foolproof if used irresponsibly.
- **Ethical Considerations** 🤝: The tool should be used for educational purposes or for improving your bot's performance and resilience. Abusing this tool for malicious purposes is unethical and illegal.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

