"""
# Daily Stock Update Email Script

This Python script retrieves stock data from Yahoo Finance for a specified list of companies, formats it into an email body, and sends a daily email update. The email includes details like the current price, 52-week high and low, and daily percentage change.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your machine.
- **Required Libraries**: `smtplib`, `email`, and `yfinance`. The `smtplib` and `email` libraries come with Python, but you’ll need to install `yfinance` if you don’t already have it.

### Installing `yfinance`

Install the `yfinance` library by running:

```bash
pip install finance
