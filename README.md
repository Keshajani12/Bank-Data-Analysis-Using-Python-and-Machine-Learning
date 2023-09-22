# Bank Data Analysis Using Python and Machine Learning

This Python script utilizes various data analysis and machine learning techniques to analyze a dataset from the banking domain. 

# Table of Contents
1. Introduction
2. Installation
3. Usage
4. Data Source
5. Data Filtering
6. Data Visualization
7. Linear Regression Model
8. Conclusion
9. Screenshots

# Introduction
The dataset, named 'bank-full.csv,' contains valuable information related to customers, including their ages, job types, marital statuses, account balances, and more. By applying data manipulation, visualization, and machine learning, this code aims to provide insights into customer behavior and predict certain outcomes based on the available data. It covers the following tasks:

 ● Loading data from a CSV file. 
 ● Data cleaning and preprocessing. 
 ● Filters the data into subsets based on age and marital status, allowing for more focused analysis of specific customer groups.  
 ● Creating various plots using Matplotlib and Seaborn for data visualization. 
 ● For predictive modeling, the script employs linear regression, utilizing customer age as a predictor for account balances. 

# Installation
1. Clone this repository: git clone https://github.com/
2. Navigate to the project directory: cd BankData
3. Install the required Python packages using pip: pip install pandas numpy matplotlib seaborn scikit-learn

# Or
Download Zip and Install requirements.txt write command : pip install -r requirements.txt

# Usage
1. Run the Python script: python bank.py
2. The script will load the Bank-full data, perform analysis, generate plots, and display them.

Importing Libraries: The script starts by importing essential libraries such as Pandas for data manipulation, Matplotlib and Seaborn for data visualization, and Scikit-Learn for machine learning tasks.

# Data Source 
It loads the banking dataset from a CSV file ('bank-full.csv') into a Pandas DataFrame and prints out some basic information about the dataset, including its shape, summary statistics, and info.

# Data Filtering
The script filters the data into different subsets based on age and marital status, creating DataFrames for 'oldAge,' 'youngster,' 'married,' 'single,' and 'divorced' customers. It provides a brief overview of each subset's content and size.

# Data Visualization

● Bar Plot: It creates a Seaborn bar plot showing the relationship between job types and account balances for older customers.
● Line Plot: Another Seaborn line plot illustrates the relationship between job types and customer ages.
● Count Plot: A Seaborn count plot displays the distribution of marital status among customers.
● Data Splitting: The dataset is split into training and testing sets for machine learning purposes. It uses the 'age' feature to predict 'balance'. It prints a preview of the split data.

# Linear Regression Model
A linear regression model is trained using the training data to predict 'balance' based on 'age.' Predictions are made on the test data, and mean squared error is computed and displayed.

● Line Plot: A line plot using Seaborn is created to visualize the actual and predicted 'balance' values.

# Conclusion
 This code provides a comprehensive analysis of the banking dataset, including data filtering, visualization, and machine learning. It can serve as a valuable reference for data analysis and predictive modeling tasks in the banking domain.

#   Screenshots