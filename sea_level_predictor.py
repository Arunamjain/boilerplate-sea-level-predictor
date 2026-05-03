import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Line of best fit using ALL data (1880 to 2050)
    slope1, intercept1, r1, p1, se1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = range(df['Year'].min(), 2051)
    sea_level_pred1 = [slope1 * year + intercept1 for year in years_extended1]
    ax.plot(years_extended1, sea_level_pred1, color='blue', label='Best Fit (All Data)')

    # Line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_extended2 = range(2000, 2051)
    sea_level_pred2 = [slope2 * year + intercept2 for year in years_extended2]
    ax.plot(years_extended2, sea_level_pred2, color='red', label='Best Fit (2000 onwards)')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig
