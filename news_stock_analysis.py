import os
import requests
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from transformers import pipeline
from bs4 import BeautifulSoup

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to fetch and summarize news articles
def fetch_and_summarize_news(query, api_key, max_articles=5):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        
        summarized_articles = []
        for article in articles[:max_articles]:
            try:
                content = article.get("content")
                if not content:
                    page_response = requests.get(article.get("url"))
                    soup = BeautifulSoup(page_response.content, 'html.parser')
                    content = ' '.join(p.text for p in soup.find_all('p'))
                
                if content:
                    summary = summarizer(content[:1024], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                    summarized_articles.append({
                        "title": article.get("title"),
                        "url": article.get("url"),
                        "summary": summary
                    })
            except Exception as e:
                print(f"Error summarizing article: {e}")
        return summarized_articles
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

# Function to fetch stock data and plot Bollinger Bands
def fetch_and_plot_stock(symbol, period):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        if data.empty:
            print("No data found for the given symbol and period.")
            return

        # Calculate Bollinger Bands
        data['RollingMean'] = data['Close'].rolling(window=20).mean()
        data['UpperBand'] = data['RollingMean'] + 2 * data['Close'].rolling(window=20).std()
        data['LowerBand'] = data['RollingMean'] - 2 * data['Close'].rolling(window=20).std()

        # Plot the stock data with Bollinger Bands
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label='Close Price', color='blue')
        plt.plot(data['RollingMean'], label='Rolling Mean', color='orange')
        plt.fill_between(data.index, data['UpperBand'], data['LowerBand'], color='gray', alpha=0.3)
        plt.title(f"{symbol} Stock Prices with Bollinger Bands")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

        print(f"Latest Closing Price: {data['Close'][-1]:.2f}")
        print(f"High: {data['High'][-1]:.2f}, Low: {data['Low'][-1]:.2f}, Volume: {data['Volume'][-1]}")
    except Exception as e:
        print(f"Error fetching or plotting stock data: {e}")

# Function to run Monte Carlo simulations for stock prices
def monte_carlo_simulation(symbol, period, days, simulations):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)
        if data.empty:
            print("No data found for the given symbol and period.")
            return

        daily_returns = data['Close'].pct_change().dropna()
        mean_return = daily_returns.mean()
        std_dev = daily_returns.std()

        last_price = data['Close'][-1]
        simulated_prices = np.zeros((simulations, days))

        for i in range(simulations):
            prices = [last_price]
            for _ in range(days - 1):
                next_price = prices[-1] * np.exp(np.random.normal(mean_return, std_dev))
                prices.append(next_price)
            simulated_prices[i] = prices

        plt.figure(figsize=(10, 5))
        for i in range(simulations):
            plt.plot(simulated_prices[i], color='gray', alpha=0.5)
        plt.title(f"Monte Carlo Simulation for {symbol}")
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.show()

        print(f"Expected Price after {days} days: {np.mean(simulated_prices[:, -1]):.2f}")
        print(f"95% Confidence Interval: {np.percentile(simulated_prices[:, -1], [2.5, 97.5])}")
    except Exception as e:
        print(f"Error running Monte Carlo simulation: {e}")

# Main function to interact with the user
def main():
    news_api_key = os.getenv("NEWS_API_KEY", "your_news_api_key")
    print("Choose an option: 1) News Summary 2) Stock Analysis 3) Monte Carlo Simulation")
    choice = input("Enter your choice: ")

    if choice == "1":
        query = input("Enter search query: ")
        articles = fetch_and_summarize_news(query, news_api_key)
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Summary: {article['summary']}")
            print("-" * 50)

    elif choice == "2":
        symbol = input("Enter stock symbol: ")
        period = input("Enter period (e.g., 1mo, 6mo, 1y): ")
        fetch_and_plot_stock(symbol, period)

    elif choice == "3":
        symbol = input("Enter stock symbol: ")
        period = input("Enter period (e.g., 1mo, 6mo, 1y): ")
        days = int(input("Enter number of days to simulate: "))
        simulations = int(input("Enter number of simulations: "))
        monte_carlo_simulation(symbol, period, days, simulations)

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
