import streamlit as st
from news_stock_analysis import fetch_and_summarize_news, monte_carlo_simulation
# from Bollinger_Bands import plot_bollinger_bands

st.set_page_config(page_title="📈 Stock Analysis Toolkit", layout="wide")

st.title("📈 Stock Analysis & Market Insights")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio("Choose a feature", ["News Summary", "Stock Analysis", "Monte Carlo Simulation"])

# NEWS
if option == "News Summary":
    st.header("📰 News Summarizer")
    query = st.text_input("Enter a topic or company name:", "technology")
    if st.button("Fetch News"):
        with st.spinner("Fetching and summarizing articles..."):
            api_key = st.secrets["NEWS_API_KEY"]
            articles = fetch_and_summarize_news(query, api_key)

            for i, article in enumerate(articles):
                st.subheader(f"{i+1}. {article['title']}")
                st.markdown(f"[Read More]({article['url']})")
                st.write(article['summary'])

# STOCK ANALYSIS
# elif option == "Stock Analysis":
#     st.header("📊 Stock Price Analysis with Bollinger Bands")
#     ticker = st.text_input("Enter Stock Symbol:", "AAPL")
#     period = st.selectbox("Select period:", ["1mo", "3mo", "6mo", "1y", "2y"], index=3)
#     if st.button("Analyze"):
#         with st.spinner("Loading chart..."):
#             plot_bollinger_bands(ticker, period)
elif option == "📊 Stock Analysis":
    st.header("📊 Stock Analysis with Bollinger Bands")
    st.info("This feature is currently under development and will be re-enabled soon.")


# MONTE CARLO
elif option == "Monte Carlo Simulation":
    st.header("🎲 Monte Carlo Simulation for Stock Forecasting")
    ticker = st.text_input("Stock Symbol:", "AAPL")
    period = st.selectbox("Historical Period:", ["1mo", "3mo", "6mo", "1y", "2y"], index=3)
    days = st.slider("Days to Simulate", min_value=30, max_value=365, value=180)
    simulations = st.slider("Number of Simulations", min_value=100, max_value=1000, step=100, value=500)
    if st.button("Run Simulation"):
        with st.spinner("Simulating future prices..."):
            monte_carlo_simulation(ticker, period, days, simulations)

