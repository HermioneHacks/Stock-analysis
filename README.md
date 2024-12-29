# Stock-analysis
This Python tool provides three main functionalities: fetching and summarizing news articles, performing stock analysis, and running Monte Carlo simulations on stock prices. The tool interacts with the user via a simple command-line interface.
# Features:

    News Summary
    Fetches news articles based on a search query and summarizes them using a pre-trained summarization model (BART).
        Input: Search query (e.g., "technology news").
        Output: Titles, URLs, and summarized content of up to 5 articles.

    Stock Analysis (Bollinger Bands)
    Fetches historical stock data for a given symbol and period (e.g., 1 month, 1 year). It then plots the stock price along with the Bollinger Bands, showing price volatility.
        Input: Stock symbol (e.g., "AAPL") and period (e.g., "1y").
        Output: Stock price chart with Bollinger Bands, latest closing price, high, low, and volume.

    Monte Carlo Simulation
    Runs simulations to predict future stock prices based on historical data and volatility. It simulates multiple paths of stock prices over a specified number of days and displays the distribution of the results.
        Input: Stock symbol, period, number of days to simulate, and number of simulations.
        Output: Monte Carlo simulation chart and statistics (expected price and 95% confidence interval).

# Setup:

    Install dependencies:

pip install requests yfinance numpy matplotlib transformers beautifulsoup4

Get an API key from NewsAPI for fetching news articles.

Set the environment variable for the NewsAPI key (or replace "your_news_api_key" in the code):

    export NEWS_API_KEY="your_news_api_key"

# Usage:

Run the script and select one of the options:

    Fetch and summarize news articles.
    Analyze stock data and plot Bollinger Bands.
    Run Monte Carlo simulations on stock prices.

# Example Interaction:

Choose an option: 1) News Summary 2) Stock Analysis 3) Monte Carlo Simulation
Enter your choice: 2
Enter stock symbol: AAPL
Enter period (e.g., 1mo, 6mo, 1y): 1y

This tool is a simple yet powerful way to analyze both financial data and news for decision-making or just for exploring market trends.
