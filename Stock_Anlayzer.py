import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class StockAnalyzer:
    def __init__(self, ticker):
        """Initialize the StockAnalyzer class with a stock ticker."""
        self.ticker_symbol = ticker
        self.ticker = yf.Ticker(ticker)

    def get_historical_data(self, period="1y"):
        """Fetch historical stock data."""
        data = self.ticker.history(period=period)
        if data.empty:
            print("\n❌ Error: No data found. Please check the ticker symbol.\n")
            return None
        return data

    def calculate_moving_averages(self, period="1y"):
        """Calculate moving averages (20-day & 50-day)."""
        data = self.get_historical_data(period)
        if data is None:
            return None
        
        data["MA_20"] = data["Close"].rolling(window=20).mean()
        data["MA_50"] = data["Close"].rolling(window=50).mean()
        return data

    def calculate_rsi(self, period="1y", window=14):
        """Calculate the Relative Strength Index (RSI)."""
        data = self.get_historical_data(period)
        if data is None:
            return None

        delta = data["Close"].diff()
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        avg_gain = pd.Series(gain).rolling(window=window, min_periods=1).mean()
        avg_loss = pd.Series(loss).rolling(window=window, min_periods=1).mean()

        rs = avg_gain / avg_loss
        data["RSI"] = 100 - (100 / (1 + rs))

        return data

    def generate_trade_signals(self, period="1y"):
        """Generate buy/sell signals based on MA & RSI."""
        data = self.calculate_moving_averages(period)
        data = self.calculate_rsi(period)

        if data is None or "MA_20" not in data or "MA_50" not in data or "RSI" not in data:
            print("\n❌ Error: Missing required data columns for trade signals.\n")
            return None

        data["Buy_Signal"] = (data["MA_20"] > data["MA_50"]) & (data["RSI"] < 30)
        data["Sell_Signal"] = (data["MA_20"] < data["MA_50"]) & (data["RSI"] > 70)

        return data

    def plot_trade_signals(self, period="1y"):
        """Plot buy/sell signals on stock price chart."""
        data = self.generate_trade_signals(period)
        if data is None:
            return

        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data["Close"], label="Close Price", color="blue", linewidth=2)

        plt.scatter(data.index[data["Buy_Signal"]], data["Close"][data["Buy_Signal"]], label="Buy Signal", marker="^", color="green", alpha=1, zorder=5)
        plt.scatter(data.index[data["Sell_Signal"]], data["Close"][data["Sell_Signal"]], label="Sell Signal", marker="v", color="red", alpha=1, zorder=5)

        plt.title(f"{self.ticker_symbol} Buy/Sell Signals")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_support_resistance(self, period="1y"):
        """Plot support and resistance levels."""
        data = self.get_historical_data(period)
        if data is None:
            return

        high = data["High"].rolling(window=20).max()
        low = data["Low"].rolling(window=20).min()

        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data["Close"], label="Close Price", color="blue", linewidth=2)
        plt.plot(data.index, high, label="Resistance Level", linestyle="--", color="red")
        plt.plot(data.index, low, label="Support Level", linestyle="--", color="green")

        plt.title(f"{self.ticker_symbol} Support & Resistance Levels")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.legend()
        plt.grid()
        plt.show()

    def position_sizing(self, capital):
        """Recommend how much to buy/sell based on capital."""
        data = self.get_historical_data(period="1mo")
        if data is None:
            return

        last_close = data["Close"].iloc[-1]
        risk_per_trade = 0.02 * capital  # 2% risk per trade
        stop_loss = last_close * 0.95  # 5% stop-loss
        position_size = risk_per_trade / (last_close - stop_loss)

        print(f"\n🔹 Suggested Position Size:")
        print(f"Stock: {self.ticker_symbol}")
        print(f"Current Price: ${last_close:.2f}")
        print(f"Recommended Quantity to Buy/Sell: {int(position_size)} shares\n")

def main():
    ticker_symbol = input("Enter stock ticker symbol (e.g. AAPL): ").upper()
    analyzer = StockAnalyzer(ticker_symbol)

    while True:
        print("\n📊 Stock Market Analyzer")
        print("1️⃣ View Stock Info")
        print("2️⃣ Plot Stock Price & Moving Averages")
        print("3️⃣ Plot Buy & Sell Signals")
        print("4️⃣ Plot Support & Resistance Levels")
        print("5️⃣ Position Sizing Recommendation")
        print("6️⃣ Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == "1":
            print(analyzer.get_historical_data(period="1y"))
        elif choice == "2":
            analyzer.plot_trade_signals(period="1y")
        elif choice == "3":
            analyzer.plot_trade_signals(period="1y")
        elif choice == "4":
            analyzer.plot_support_resistance(period="1y")
        elif choice == "5":
            capital = float(input("Enter your trading capital: $"))
            analyzer.position_sizing(capital)
        elif choice == "6":
            print("Exiting... Have a great trading day! 🚀")
            break
        else:
            print("❌ Invalid choice, please select again.")

if __name__ == "__main__":
    main()
