## TITLE: 
Main Flow Services and Technologies Internship - Task Documentation: Data Manipulation with Pandas (Jupyter Notebook).

### DESCRIPTION:
This task involves using the Pandas library to manipulate data.

### RESPONSIBILITY:
Load a CSV file into a Pandas DataFrame. Perform operations like filtering data based on conditions, handling missing values, and calculating summary statistics.

## INTERN INFORMATION:

**Name:** Yash Sanjay Kadyan

**ID:** ID-11896


# INTRODUCTION

In the realm of data analysis and preprocessing, handling and cleaning datasets is a critical step to ensure accurate and meaningful results. This code provides a comprehensive demonstration of various techniques for inspecting, cleaning, and processing a dataset using Python's Pandas library.

First, the code imports the Pandas library, a powerful tool for data manipulation, and loads a CSV file into a DataFrame. It then uses the type function to confirm that the data is stored in a DataFrame and the info function to display detailed information about the dataset, including the data types of each column and the presence of null values.

To understand the structure of the dataset, the shape function reveals that it contains 324 rows and 23 columns. The describe function provides basic descriptive statistics, offering insights into the distribution and central tendencies of the data.

Duplicate rows are removed using the drop_duplicates function, ensuring that each entry in the dataset is unique. The isnull function identifies missing values, and isnull().sum() calculates the total number of null values in each column. The notnull function, on the other hand, checks for non-null values.

Various methods for handling missing values are demonstrated. The fillna function replaces null values with a specified value, such as 0 or 3, effectively filling gaps in the dataset. Forward filling (ffill) and backward filling (bfill) techniques are also illustrated, which propagate the last valid observation or the next valid observation, respectively, to fill in missing values.

For detecting and removing outliers, the code employs the Inter-Quartile Range (IQR) method. By calculating the first (Q1) and third quartiles (Q3), and subsequently the IQR, the code identifies outliers as data points falling outside 1.5 times the IQR from the lower and upper quartiles. These outliers are then removed to ensure a clean dataset.

Finally, the code drops non-numeric columns, such as 'Observation', to focus on numeric data for further analysis. The cleaned dataset, free from missing values and outliers, is then summarized using the describe function to provide updated descriptive statistics.

Through these steps, the code offers a thorough overview of essential data cleaning and preprocessing techniques in Python, equipping you with the foundational skills needed for effective data analysis.


# Implementation

• Pandas DataFrames: Utilize Pandas' DataFrame structure to load, inspect, and manipulate tabular data efficiently. This includes reading data from CSV files and performing basic data exploration.

• Data Inspection: Employ Pandas functions such as info(), shape, and describe() to gain insights into the dataset's structure, size, and basic statistics. These functions help identify the presence of missing values and understand the distribution of data.

• Handling Missing Values: Implement techniques to handle missing values using Pandas' isnull(), fillna(), ffill(), and bfill() functions. These methods allow for replacing or filling in gaps in the dataset to ensure completeness.

• Removing Duplicates: Use the drop_duplicates() function to eliminate duplicate rows, ensuring each entry in the dataset is unique and avoiding redundant information.

• Outlier Detection and Removal: Apply the Inter-Quartile Range (IQR) method to detect and remove outliers. Calculate the IQR and identify data points that fall outside the acceptable range, cleaning the dataset from extreme values that could skew analysis.

• Column Management: Drop non-numeric columns using the drop() function to focus on numeric data for further analysis. This helps in performing numerical operations and statistical analysis effectively.

• Descriptive Statistics: Use the describe() function on the cleaned dataset to get updated descriptive statistics, providing a summary of the central tendency, dispersion, and shape of the data distribution.

Through these implementations, the code showcases a comprehensive approach to data cleaning and preprocessing, essential for accurate and meaningful data analysis in Python using the Pandas library.


# CODE EXPLANATION



# Pandas DataFrames:

## Data Loading and Initial Exploration:

### • Importing the Pandas Library:

import pandas as pd

• Imports the Pandas library, a powerful tool for data manipulation and analysis.

### • Loading a CSV File:

data = pd.read_csv('E:\\Main Flow Services and Technologies\\TASKS\\DATA_ANALYSIS_WITH_PYTHON-ID-11896\\TASK 2\\01.Data Cleaning and Preprocessing.csv')

• Loads a CSV file into a DataFrame named data using the read_csv function.

### • Checking Data Type:

type(data)

• Confirms that the data is stored in a Pandas DataFrame.

### • Getting Data Information:

data.info

• Displays detailed information about the DataFrame, including data types and null value counts.

### • Checking Data Shape:

data.shape

• Returns the number of rows and columns in the DataFrame: (324, 23).

### • Descriptive Statistics:

data.describe()

• Provides basic descriptive statistics for numerical columns in the DataFrame.


## Data Cleaning:

### • Dropping Duplicates:

data.drop_duplicates()

• Removes duplicate rows from the DataFrame.

### • Checking for Null Values:

data.isnull().sum()

• Calculates the total number of null values in each column.

### • Total Null Values:

data.isnull().sum().sum()

• Calculates the total number of null values in the entire DataFrame.

### • Filling Null Values:

data2 = data.fillna(value=0)

• Replaces all null values in the DataFrame with 0.

data2 = data.fillna(value=3)

• Replaces all null values in the DataFrame with 3.

### • Forward Filling Null Values:

data3 = data.ffill()

• Fills null values with the previous non-null value in the DataFrame.

### • Backward Filling Null Values:

data4 = data.bfill()

• Fills null values with the next non-null value in the DataFrame.


## Outlier Detection and Removal:

### • Calculating IQR:

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

• Computes the Inter-Quartile Range (IQR) to identify the range of acceptable values.

### • Removing Outliers:

data2 = data2[~((data2 < (Q1 - 1.5 * IQR)) | (data2 > (Q3 + 1.5 * IQR))).any(axis=1)]

• Removes rows with outlier values outside the 1.5 * IQR range.


## Column Management:

### • Dropping Non-Numeric Columns:

data2.drop(['Observation'], axis=1, inplace=True)

• Removes the 'Observation' column, focusing on numeric data.


## Final Descriptive Statistics:

### • Updated Descriptive Statistics:

data2.describe()

• Provides updated descriptive statistics for the cleaned dataset, reflecting the changes made during data cleaning.

This code offers a step-by-step approach to data loading, exploration, cleaning, and preprocessing using Pandas, ensuring a clean and well-structured dataset for analysis.


# USAGE

**Loading Data into a DataFrame:** Users can load a CSV file into a Pandas DataFrame using the `read_csv` method, which allows for efficient data manipulation and analysis.

data = pd.read_csv('path/to/your/file.csv')


**Checking Data Type:** Users can confirm that their data is stored in a DataFrame by using the `type` function.

type(data)

**Inspecting Data Information:** Users can use the `info` method to display detailed information about the DataFrame, including data types and null values.

data.info

**Checking Data Shape:** Users can determine the number of rows and columns in their DataFrame using the `shape` attribute.

data.shape

**Descriptive Statistics:** Users can obtain basic descriptive statistics of their dataset using the `describe` method.

data.describe()

**Removing Duplicate Rows:** Users can eliminate duplicate rows in their DataFrame using the `drop_duplicates` method.

data.drop_duplicates()

**Identifying Null Values:** Users can check for null values in their DataFrame using the `isnull` method, which returns a DataFrame indicating the presence of null values.

data.isnull()

**Counting Null Values per Column:** Users can count the total number of null values in each column using the `isnull().sum()` method.

data.isnull().sum()

**Total Null Values:** Users can calculate the total number of null values in the entire DataFrame using `isnull().sum().sum()`.

data.isnull().sum().sum()

**Filling Null Values:** Users can fill null values in their DataFrame with a specific value using the `fillna` method.

data2 = data.fillna(value=0)

**Forward Filling Null Values:** Users can fill null values with the previous non-null value using the `ffill` method.

data3 = data.ffill()

**Backward Filling Null Values:** Users can fill null values with the next non-null value using the `bfill` method.

data4 = data.bfill()

**Calculating IQR for Outlier Detection:** Users can calculate the Inter-Quartile Range (IQR) to identify the range of acceptable values in their data.

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

**Removing Outliers:** Users can remove outliers from their DataFrame using the IQR method to ensure data falls within an acceptable range.

data2 = data2[~((data2 < (Q1 - 1.5 * IQR)) | (data2 > (Q3 + 1.5 * IQR))).any(axis=1)]

**Dropping Non-Numeric Columns:** Users can remove non-numeric columns to focus on numeric data for further analysis using the `drop` method.

data2.drop(['Observation'], axis=1, inplace=True)

**Updated Descriptive Statistics:** Users can obtain updated descriptive statistics of their cleaned dataset using the `describe` method.

data2.describe()



# CONCLUSION

In conclusion, this Python code example effectively demonstrates essential data cleaning and preprocessing techniques using the Pandas library. By guiding users through loading data into a DataFrame, inspecting the dataset, handling missing values, and detecting and removing outliers, the code provides a comprehensive foundation for preparing data for analysis. These steps are crucial for ensuring the quality and integrity of the dataset, which directly impacts the accuracy and reliability of any subsequent analysis. By mastering these techniques, users can confidently manage and preprocess data, paving the way for more sophisticated data analysis and machine learning tasks. With continued practice and exploration of these methods, users can enhance their data manipulation skills and develop robust, efficient solutions for a wide range of data-driven challenges.

# OUTPUT

![Loading CSV File into Pandas DataFrame using the read_csv() function and using the type() and info functions](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/2211f36f-cc93-4e73-8f7b-20efd837df91")

![Loading CSV File into Pandas DataFrame](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/584c4919-2370-41e4-a2d5-7d8d6600cdc1)

![Loading CSV File into Pandas DataFrame](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/5c079496-d789-4237-8891-8900022a1161)

![Using the shape and describe() functions on the dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/e0b164e0-a499-4f46-8302-8490bcb82f4f)

![Using the drop_duplicates() function on the dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/ed0e00d3-afb5-4bc6-bf93-5be84dc97efa)

![Using the isnull() function](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/47449f89-8413-4729-85da-5796faa25a55)

![Using the isnull() function](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/4574d967-c32d-4973-94e1-cf7c6b17ea3b)

![Using the isnull().sum() function](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/906b0455-6fb7-4a33-b017-8e95ed57ff7f)

![Using the notnull() function](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/59b30b50-4aab-44bf-9867-2e7a145334a1)

![Using the isnull().sum().sum() to get the total null values in the dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/eecb6b54-9886-4796-aada-551ceda8b7eb)

![Method 1 for Filling the Null Values in the dataset with value as 0](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/e7abe028-03da-4a70-b70e-8789c1a8023f)

![Method 1 for Filling the Null Values in the dataset with value as 3](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/46a2816e-6681-4227-8be4-7d665f63c241)

![Using the isnull().sum().sum() to get the total null values in the dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/ffd7c36f-4fb0-48cb-8f9e-2b3d482118f5)

![Displaying the data which is a DataFrame of the Dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/04bf2744-bab9-4506-a0d0-176aba30e6a8)

![Method 2 for Filling the Null Values in the dataset (Forward Filling - Filling Null Values with the previous value in our Dataset)](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/4c61e203-4a68-4b37-9935-34fd98082868)

![Method 3 for Filling the Null Values in the dataset (Backward Filling - Filling Null Values with the next value in our Dataset)](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/7c81106f-18c4-4032-8d8b-8317df7bc94d)

![Using numpy library for handling our numeric Dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/45da13dd-4b50-42bb-a4d9-fbafa021dcdf)

![Importing matplotlib library, stats library from scipy and Detecting the Outliers in our Dataset using IQR](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/de2ae7f8-0585-4ef6-859f-a0ae852abb16)

![Using the drop() function for dropping the 'Observation' column since it contains a String in Date-Time format](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/31683217-627f-47ce-805a-f452e1ab7360)

![Checking the Outliers using the IQR (Inter-Quartile Range) Method](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/8723bff3-f73a-44e0-ac3e-a6973cd8939f)

![Removing the Detected Outliers using Formula](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/9ef52760-4253-4f2a-a620-9701563161dc)

![Displaying our data2 DataFrame of the dataset once the detected outliers are removed and we get a clean form of our Dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/d9ed8dce-d4bf-408a-b035-d348c00566cf)

![Using the describe() function to get a proper descriptive statistics of our cleaned Dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/dc8b49c5-026b-4203-9df8-2b1ae19ee1fd)

![Calculating and Displaying the Proper Summary Statistics after getting our cleaned Dataset](https://github.com/YashKadyan/DATA_ANALYSIS_WITH_PYTHON-ID-11896/assets/66464974/828004ab-375b-4fcb-86a6-f1ece0e7c438)
