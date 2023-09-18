# INF601 - Advanced Programming in Python
# Nikhil Dhage
# Mini Project 1

import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using an API of your choice (yfinance works), collect the closing price of
# 5 of your favorite stock tickers for the last 10 trading days.
# (10/10 points) Store this information in a list that
# you will convert to a array in NumPy.
# (10/10 points) Plot these 5 graphs. Feel free to add as much information to
# the graphs as you like exploring the documentation for matplotlib. At minimum, it just needs to show 10 data points.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project
# folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this file with the output of pip freeze at
# the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project
# is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

# Returns a list of the stock closing prices
def getClosing(ticker: str) -> list:
    # getting stock data
    stock = yf.Ticker(ticker)
    # get historical market data
    hist = stock.history(period="10d")

    # Create empty closing list
    closingList = []

    # Loop through hist info and appends all closing prices to closing list
    for price in hist['Close']:
        closingList.append(round(price, 2))

    return closingList


def showGraphs():
    # stocks list
    stocks = ["MSFT", "AAPL", "GME", "SONY", "META"]

    for stock in stocks:
        # empty numpy array created from returned closing price list
        stockClosing = np.array(getClosing(stock))

        # list of days for plot
        days = list(range(1, len(stockClosing) + 1))

        # Plot the graphs
        plt.plot(days, stockClosing)

        # get low and high closing price
        prices = getClosing(stock)
        prices.sort()
        low_price = prices[0]
        high_price = prices[-1]

        # set x and y axis min and max
        plt.axis([1, 10, low_price, high_price])

        # Setup graph title and labels
        plt.title("Closing Price for" + " " + stock)
        plt.xlabel("Days")
        plt.ylabel("Closing Price")

        # save Graphs to charts folder
        saveFile = "charts/" + stock + ".png"
        plt.savefig(saveFile)

        # Show graphs
        plt.show()


showGraphs()
