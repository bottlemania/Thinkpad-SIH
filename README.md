# Thinkpad-SIH
A repo to host the code involved in Thinkpad's solution<br><br>**Explanation**

* Pandas library is imported to read the csv file and to convert the csv file into Dataframe.
*	Sklearn:
     -	To spilt the data frame into testing and training set.
     -	To import Decision tree Regression model, Random Forest Regression          model and SVR regression Model.
     -	To calculate Mean absolute error, Mean squared error and r square value.

*	Xgboost library is used to import XGRegression.

- 1st, the csv file is read and converted into Data frame and stored in variable named data.
- data.shape provide the size of the data frame.
- data.describe() provide information about,

  Count: The number of non-null (non-missing) values.
  Mean (Average): The average value of the data.
  Standard Deviation: A measure of the data's spread or dispersion.
  Minimum: The smallest value in the dataset.
  25th Percentile: The value below which 25% of the data falls (also known    as the first quartile).
  Median (50th Percentile): The middle value when the data is sorted.
  75th Percentile: The value below which 75% of the data falls (also known    as the third quartile).
  Maximum: The largest value in the dataset.
  
  Data Type Information: It typically includes information about the data     types of each column, such as whether a column contains numeric data,       categorical data, or dates.
   
  Handling Missing Values: It may also indicate the count of missing (null    or NaN) values in each column.
   
  Data Range: It provides an overview of the range of values within each      column, which can be useful for understanding the data's distribution.
   
  Percentiles: The method often includes percentiles, such as the 25th and    75th percentiles, which help you understand the data's distribution and     identify potential outliers.

*	1D array data of MAGON AND MAGLAT of data frame is converted to 2D array data. And it was stored in variable X and y.
*	Using train_test_split the whole data frame was splitted into training and test data set, such way that 70% of total data was used as training data set and remaining 30% data set is used test data set.
*	Training and test data set is fitted to all four regression models.
*	Errors and R square value was calculated for all Regression model.
*	If the value of absolute error value and mean square value is very less means Regression model is better.
*	The value of R square vale ranges from 0 to1 and if it’s value is greater than 0.9 the regression model is better.<br>
Here, for decision tree and Random Forest the error values are very smaller and R squared value is 1.
<br>Thus, either Decision tree or Random Forest can be used for prediction of volume of magnetic materials present which had created magnetic anomaly.



 



