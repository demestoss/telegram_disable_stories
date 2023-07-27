# Block all Stories in Telegram

## Installation

1. Install python >3.10

2. Install all dependencies
```
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and provide Telegram `api_id` and `api_hash`. You can find them using the next guide

4. Run 
```
python3 main.py
```

## Get Telegram API keys

1. [Login to your Telegram](https://my.telegram.org/auth) account with the phone number of the developer account to use.

2. Click under API Development tools.

3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.

4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!
