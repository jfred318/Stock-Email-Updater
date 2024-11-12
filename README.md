# Daily Stock Update Email Script

This Python script retrieves stock data from Yahoo Finance for a specified list of companies, formats it into an email body, and sends a daily email update. The email includes details like the current price, 52-week high and low, and daily percentage change.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine.
- **Required Libraries**: `smtplib`, `email`, and `yfinance`. The `smtplib` and `email` libraries come with Python, but you’ll need to install `yfinance` if you don’t already have it.

### Installing `yfinance`

Install the `yfinance` library by running:

```bash
pip install finance
```

## Getting Started
**Define Sender and Receiver Emails:**

- Replace User_Email in the script with your Gmail address (for both sender and receiver).


- Replace User_App_Password with the App Password created for your Gmail account

```bash
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
sender_password = "your_app_password"
```

## Usage
Execute the Script: Run the script from your terminal or command prompt:

```bash
python daily_stock_update.py
```

Check for the Email: The script will send an email to the specified receiver with the latest stock data.

**Common Errors:**

SMTP Authentication Error: 
- Ensure your email and app password are correct.
- Other Exceptions: The script will print any other errors encountered.

