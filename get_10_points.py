import random

# Function to return 10 consecutive data points starting from a random timestamp
def get_10_points(stock_ids, timestamps, stock_prices):
    # Set the last possible start point as the 10th point counting backwards
    last_valid_start = len(stock_prices) - 10
    # Get a random start point
    start_point = random.randrange(last_valid_start)
    # Set the end point to get exactly 10 values
    end_point = start_point + 10

    # Return the 10 consecutive data points and 3 more spots in the timeseries to be filled with predictions
    return (stock_ids[start_point:(end_point + 3)], timestamps[start_point:(end_point + 3)], stock_prices[start_point:end_point])