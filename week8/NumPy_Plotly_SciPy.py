# Import necessary libraries
import numpy as np
import plotly.graph_objects as go
from scipy import stats

# NumPy Functionality
## Create a numpy array
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array: ", np_array)

## Perform basic mathematical operations
print("Mean: ", np.mean(np_array))
print("Median: ", np.median(np_array))
print("Standard Deviation: ", np.std(np_array))

# Plotly Functionality
## Create a line plot
fig = go.Figure(data=go.Scatter(x=np_array, y=np_array**2))
fig.update_layout(title='Line Plot', xaxis_title='X', yaxis_title='Y')
fig.show()

# SciPy Functionality
## Perform a t-test
t_stat, p_val = stats.ttest_1samp(np_array, 3)
print("T-statistic: ", t_stat)
print("P-value: ", p_val)

## Fit a normal distribution
mean, std_dev = stats.norm.fit(np_array)
print("Mean (Normal Distribution): ", mean)
print("Standard Deviation (Normal Distribution): ", std_dev)
