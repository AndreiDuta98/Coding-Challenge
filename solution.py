import os
import csv
from get_10_points import *
from predict import *

# INPUT SECTION

# Specify the recommended number of files to be sampled for each Stock Exchange
number_of_files = 2
# Specify the path where the folder containing the stocks data is located
path = "D:\LSEG Challenge\Challenge\stock_price_data_files"

# SOLUTION 

# Get the list of stocks
stock_list = os.listdir(path)
# Iterate through each stock in the list
for stock in stock_list:
    # Get the available files for each stock
    stock_path = os.path.join(path, stock)
    stock_files = os.listdir(stock_path)
    # Use just the recommended number of files
    stock_files = stock_files[:number_of_files]

    # Process each file
    for file in stock_files:
        # Get the path to the file
        filename = os.path.join(stock_path, file)

        # Try to open the file
        try:
            with open(filename) as f:
                reader = csv.reader(f)
                header_row = next(reader)

                # Get the data (stock_id, timestamp, stock_price)
                stock_ids, timestamps, stock_prices = [], [], []
                for row in reader:
                    id = row[0]
                    time = row[1]
                    # Check if there is missing data for the price at a certain timestamp
                    try:
                        price = float(row[2])
                    except ValueError:
                        print(f"Missing data for {time}")
                    else:
                        # Add the data in a list for each column
                        stock_ids.append(id)
                        timestamps.append(time)
                        stock_prices.append(price)
                        
                # Process the data

                # Get 10 consecutive data points from a random timestamp
                stock_ids, timestamps, stock_prices = get_10_points(stock_ids, timestamps, stock_prices)
                # Predict the next 3 values
                predicted_prices = predict(stock_prices)
                # Add the predicted values to the set
                stock_prices.extend(predicted_prices)

                # Create the output files
                
                # Name of the file = name of the original file (without extension) + _prediction.csv 
                output_filename = os.path.splitext(filename)[0] + "_prediction.csv"
                # Open the file in write mode
                with open(output_filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    # Write each row of the file
                    for i in range(0, 13):
                        writer.writerow([stock_ids[i], timestamps[i], stock_prices[i]])
        
        except IOError:
            print(f"Could not read file: {file}")

            
