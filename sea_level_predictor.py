import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv', index_col=0)

    # Create scatter plot

    fig, ax= plt.subplots(figsize=(12,8))
    
    ax.scatter(df.index, 'CSIRO Adjusted Sea Level', marker='.', data = df)

    # Create first line of best fit

    res = linregress(df.index, df['CSIRO Adjusted Sea Level'])
    xrange = pd.Series(range(1880,2052))

    ax.plot(xrange, res.intercept + res.slope*xrange, 'r', linestyle='dashed')

    ax.vlines(2050, ymin=-0.5, ymax=16)
    ax.set_ylim(bottom=-1, top=17)
    ax.set_xlim(left=1875, right=2060)
    
    ax.hlines(res.intercept + res.slope*2050, xmin= 1875, xmax=2050, linestyle='dashed')

    # Create second line of best fit

    df_2000 = df.copy()
    df_2000 = df_2000.loc['2000':]

    res_new = linregress(df_2000.index, df_2000['CSIRO Adjusted Sea Level'])

    xrangenew= pd.Series(range(2000,2052))

    ax.plot(xrangenew, res_new.intercept + res_new.slope*xrangenew, 'g', linestyle='dashed')

    ax.hlines(res_new.intercept + res_new.slope*2050, xmin= 1875, xmax=2050, linestyle='dashed')

    # Add labels and title

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
