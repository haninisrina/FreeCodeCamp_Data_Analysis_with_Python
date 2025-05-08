import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = res1.intercept + res1.slope*x1
    plt.plot(x1,y1,color='firebrick')

    # Create second line of best fit
    x_ = range(2000, df["Year"].iloc[-1]+1, 1)
    slope, intercept, r_value, p_value, std_err = linregress(x_, df[-len(x_):]["CSIRO Adjusted Sea Level"])
    x2 = range(2000, 2051, 1)
    plt.plot(x2, intercept + slope*x2, 'r', label='fitted line 2')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()