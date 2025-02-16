import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def load_data(file_path):
    """Load stock data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

def prepare_data(df):
    """Prepare data for training the model."""
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace=True)
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days
    
    X = df[['Days']].values
    y = df['Close'].values
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_prices(model, X_test):
    """Make predictions using the trained model."""
    return model.predict(X_test)

def plot_results(df, X_train, y_train, X_test, y_test, predictions):
    """Plot the actual vs predicted stock prices."""
    plt.scatter(X_train, y_train, color='blue', label='Training Data')
    plt.scatter(X_test, y_test, color='red', label='Test Data')
    plt.plot(X_test, predictions, color='green', linewidth=2, label='Predicted Trend')
    plt.xlabel('Days Since Start')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

def main():
    """Main function to execute the stock prediction pipeline."""
    file_path = 'stock_data.csv'  # Update with actual file path
    df = load_data(file_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    model = train_model(X_train, y_train)
    predictions = predict_prices(model, X_test)
    
    print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
    plot_results(df, X_train, y_train, X_test, y_test, predictions)

if __name__ == "__main__":
    main()
