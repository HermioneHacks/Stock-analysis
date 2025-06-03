# Stock-analysis  
This Python web app provides two main functionalities: fetching and summarizing news articles, and running Monte Carlo simulations on stock prices. The tool interacts with the user via an intuitive, deployable Streamlit interface.

This project was created to explore market trends using financial data and NLP-powered news summarization — all in a deployable, user-interactive tool.

# Features:

    News Summary  
    Fetches news articles based on a search query and summarizes them using a pre-trained summarization model (BART).  
        Input: Search query (e.g., "technology news").  
        Output: Titles, URLs, and summarized content of up to 5 articles.

    Monte Carlo Simulation  
    Runs simulations to predict future stock prices based on historical data and volatility. It simulates multiple paths of stock prices over a specified number of days and displays the distribution of the results.  
        Input: Stock symbol, period, number of days to simulate, and number of simulations.  
        Output: Monte Carlo simulation chart and statistics (expected price and 95% confidence interval).

# Setup:

    1. Clone the repository:

git clone https://github.com/HermioneHacks/Stock-analysis.git  
cd Stock-analysis

    2. Install dependencies:

pip install -r requirements.txt

    3. Get an API key from NewsAPI:

- Go to https://newsapi.org/register  
- Sign up and verify your email  
- Copy your API key from the dashboard

    4. Set the API key locally:

export NEWS_API_KEY="your_api_key_here"

    Or, if using Streamlit Cloud, set it under:

    Settings → Secrets:

NEWS_API_KEY = "your_api_key_here"

# Usage:

    Run the Streamlit app locally:

streamlit run app.py

    Then go to:

http://localhost:8501

    Choose one of the options from the sidebar:
        - Fetch and summarize news articles.
        - Run Monte Carlo simulations on stock prices.

# Example Interaction:

    Select: "News Summary"
    Enter: technology
    → Returns summarized headlines and links

    Select: "Monte Carlo Simulation"
    Enter stock symbol: AAPL  
    Enter period: 1y  
    Enter number of days: 180  
    Enter number of simulations: 500  
    → Returns price forecast chart + 95% confidence interval

This tool is a simple yet powerful way to analyze both financial data and news for decision-making or just for exploring market trends.

# 🧠 Motivation  
This project was built to:

    Combine financial data with NLP tools

    Explore Python-based data analysis in a real-world use case

    Create a reusable, lightweight tool for investors or curious learners
