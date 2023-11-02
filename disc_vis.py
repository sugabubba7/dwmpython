#1
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {'value': [15, 28, 32, 40, 52, 58, 60, 70, 75, 80, 90, 100]}
df = pd.DataFrame(data)

# Define bin edges
bin_edges = [0, 30, 60, 100]

# Discretize the data using pandas.cut()
df['bin'] = pd.cut(df['value'], bins=bin_edges, labels=['Low', 'Medium', 'High'])

# Plot histogram
plt.figure(figsize=(8, 6))
plt.hist(df['value'], bins=bin_edges, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Value')
plt.xticks(bin_edges)
plt.show()

# Plot scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['value'], df['bin'], color='green', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Bin')
plt.title('Scatter Plot of Value vs. Bin')
plt.yticks(df['bin'].unique())
plt.show()

#2
#2
import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
