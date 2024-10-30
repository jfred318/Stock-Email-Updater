import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yfinance as yf

def send_email(subject, body, sender, receiver, password):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls() 
            server.login(sender, password)

           
            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            
            server.sendmail(sender, receiver, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Please check your email and app password.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def fetch_stock_data(tickers):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        current_price = info.get("currentPrice")
        previous_close = info.get("regularMarketPreviousClose")

        if previous_close:
            percentage_change = ((current_price - previous_close) / previous_close) * 100
        else:
            percentage_change = None  

        data[ticker] = {
            "Current Price": current_price,
            "PE Ratio": info.get("trailingPE"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
            "Percentage Change": percentage_change,
        }
    return data


subject = "Daily Stock Update"
tickers = ["NVDA", "AMZN", "GOOG", "AAPL", "MSFT", "META", "ADBE", "IBM", "TSLA"]
stock_data = fetch_stock_data(tickers)


email_body = "Here is the daily stock update:\n\n"
for ticker, info in stock_data.items():
    email_body += f"{ticker}:\n"
    email_body += f"  Current Price: ${info['Current Price']}\n"
    email_body += f"  52 Week High: ${info['52 Week High']}\n"
    email_body += f"  52 Week Low: ${info['52 Week Low']}\n"
    if info["Percentage Change"] is not None:
        email_body += f"  Percentage Change: {info['Percentage Change']:.2f}%\n"
    else:
        email_body += "  Percentage Change: Data not available\n"
    email_body += "\n"

sender_email = "User_Email"
receiver_email = "User_Email"  


sender_password = "User_App_Password"  


send_email(subject, email_body, sender_email, receiver_email, sender_password)
