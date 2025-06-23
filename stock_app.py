import streamlit as st

st.title("📈 Stock Price Predictor")
st.write("This app predicts the stock prices of a company based on historical data.")
st.write("Enter a stock ticker (like `AAPL`, `GOOG`, `MSFT`) to get the latest price and a prediction for the next day.")

ticker = st.text_input("Stock Ticker", "AAPL")
# "AAPL" is the default stock value set.

import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def get_stock_data(ticker, period='1y'):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        if df.empty:
            st.error("No data found. Try a different ticker.")
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def preprocess_data(df):
    df = df[['Close']].copy()
    df['Prediction'] = df['Close'].shift(-1)
    df.dropna(inplace=True)
    return df

def train_model(df):
    X = df[['Close']]
    y = df['Prediction']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy

def predict_next_day(model, latest_price):
    return model.predict(pd.DataFrame([[latest_price]], columns=['Close']))[0]

if st.button("Predict"):
    df = get_stock_data(ticker)
    if df is not None and not df.empty:
        df_processed = preprocess_data(df)
        model, accuracy = train_model(df_processed)
        latest_price = df_processed['Close'].iloc[-1]
        prediction = predict_next_day(model, latest_price)

        st.success(f"📌 Latest price: ${latest_price:.2f}")
        st.success(f"📌 Predicted next price: ${prediction:.2f}")
        st.info(f"✅ Model accuracy: {accuracy*100:.2f}%")

        st.line_chart(df_processed['Close'])


