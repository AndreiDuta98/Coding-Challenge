# Function to predict the next 3 values in the timeseries data
def predict(stock_prices):
    # Sort the list of prices in descending order
    descending_prices = sorted(stock_prices, reverse=True)
    # First predicted datapoint is the same as the 2nd highest value
    n_1 = descending_prices[1]
    # n+2 data point has half the difference between n and n+1
    n_2 = abs(stock_prices[-1] - n_1) / 2
    # n+3 data point has 1/4th the difference between n+1 and n+2
    n_3 = abs(n_1 - n_2) / 4
    # Put the predicted values in a list
    prediction = []
    prediction.append(n_1)
    prediction.append(round((n_2), 2))
    prediction.append(round((n_3), 2))

    # Return the list
    return prediction