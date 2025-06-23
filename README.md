
# 📈 Stock Price Predictor

A lightweight and interactive **Streamlit web app** that predicts the **next day's stock price** using **Linear Regression** based on historical data from Yahoo Finance.

---

## 🚀 Features

- 🔍 Search by stock ticker (e.g., `AAPL`, `GOOG`, `MSFT`)
- 📊 View the latest stock closing price
- 🧠 Predict the next day's price using a trained ML model
- ✅ Displays model accuracy
- 📈 Visualize stock price history in a line chart

---

## 🖥️ Demo

Live here 👉 [Launch the web app](https://stock-price-predictor-avaagdb8d4yqs5j6ea3uta.streamlit.app/)

---

## 📦 Requirements

Install required Python libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/stock-price-predictor.git
cd stock-price-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧠 How It Works

1. The app fetches 1 year of historical stock data using the `yfinance` API.
2. It focuses on the **Closing Price** to train a **Linear Regression** model.
3. The model learns to predict the next day's closing price based on today's price.
4. Streamlit displays the prediction, accuracy score, and a closing price chart.

---

## 🛠️ Technologies Used

- **Python** 🐍
- **Streamlit** – for the interactive web app UI
- **yfinance** – to fetch historical stock prices
- **pandas** – to clean and prepare the data
- **scikit-learn** – for linear regression modeling

---

## 🧑‍💻 Author

Made with ❤️ by **Joshua**

---

## ⚖️ License

This project is open-source and available under the MIT License.
