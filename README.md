# sqlalchemy-challenge
#### Module 10 Homework

For this exercise, raw data from Hawaii weather stations was reviewed and queried for various data. Using a combination of Pandas, Jupyter Notebook, and Python I have completed the assignment.

### Exploratory Precipitation Analysis:

Find the most recent date in the data set:

('2017-08-23')

Calculate the date one year from the last date in data set:

datetime.date(2016, 8, 23)

Perform a query to retrieve the data and precipitation scores

 ('2016-08-23', 0.0),
 ('2016-08-23', 0.15),
 ('2016-08-23', 0.05),
 ('2016-08-23', None),
 ('2016-08-23', 0.02),
 ('2016-08-23', 1.79),
 ('2016-08-23', 0.7),
 ('2016-08-24', 0.08),
 ('2016-08-24', 2.15),
 ('2016-08-24', 2.28)...
 
Save the query results as a Pandas DataFrame and set the index to the date column. Sort the dataframe by date:
 
  Precipitation
Date	
2016-08-23	0.00
2016-08-23	0.15
2016-08-23	0.05
2016-08-23	NaN
2016-08-23	0.02
...	...
2017-08-22	0.50
2017-08-23	0.00
2017-08-23	0.00
2017-08-23	0.08
2017-08-23	0.45

Use Pandas Plotting with Matplotlib to plot the data:

![Screenshot 2022-12-04 133242](https://user-images.githubusercontent.com/112498067/205508918-54821d5e-9512-4365-a41d-e4cc20ce61c0.png)

Use Pandas to calculate the summary statistics for the precipitation data:

Precipitation
count	2021.000000
mean	0.177279
std	0.461190
min	0.000000
25%	0.000000
50%	0.020000
75%	0.130000
max	6.700000

### Exploratory Station Analysis

Design a query to calculate the total number stations in the dataset:

9

Design a query to find the most active stations (i.e. what stations have the most rows?):

'USC00519281'

List the stations and the counts in descending order:

USC00519281 2772
USC00519397 2724
USC00513117 2709
USC00519523 2669
USC00516128 2612
USC00514830 2202
USC00511918 1979
USC00517948 1372
USC00518838 511

Using the most active station id from the previous query, calculate the lowest, highest, and average temperature:

[('USC00519281', 71.66378066378067, 85.0, 54.0)]

Using the most active station id query the last 12 months of temperature observation data for this station:

[('USC00519281', '2016-08-23', 77.0),
 ('USC00519281', '2016-08-24', 77.0),
 ('USC00519281', '2016-08-25', 80.0),
 ('USC00519281', '2016-08-26', 80.0),
 ('USC00519281', '2016-08-27', 75.0),
 ('USC00519281', '2016-08-28', 73.0),
 ('USC00519281', '2016-08-29', 78.0),
 ('USC00519281', '2016-08-30', 77.0),
 ('USC00519281', '2016-08-31', 78.0),
 ('USC00519281', '2016-09-01', 80.0),
 ('USC00519281', '2016-09-02', 80.0)...

Plot the results as a histogram:

![Screenshot 2022-12-04 133600](https://user-images.githubusercontent.com/112498067/205509049-b04e0896-1244-47b8-bfee-6318e3f05721.png)


