import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("sea-level.csv")
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    plt.scatter(x, y)

    # Create first line of best fit
    lineA = linregress(x, y)
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = x1*lineA.slope + lineA.intercept

    plt.plot(x1,y1,'blue')

    # Create second line of best fit
    df_2 = df.loc[df['Year'] >= 2000]

    lineB = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2051,1)
    y2 = x2*lineB.slope + lineB.intercept

    plt.plot(x2,y2,'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()