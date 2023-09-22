import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Get data from csv file
df = pd.read_csv('BankData/bank-full.csv')
print(df.head())
print(df.shape)
print(df.describe())
print(df.info)

oldAge = df[df.age >=50]
print(oldAge.head())
print(oldAge.shape)

youngster = df[df.age<50]
print(youngster.head())
print(youngster.shape)

married = df[df.marital == 'married']
print(married.head())
print(married.shape)

single = df[df.marital == 'single']
print(single.head())
print(single.shape)

divorced = df[df.marital == 'divorced']
print(divorced.head())
print(divorced.shape)

# Create a Bar plot using Seaborn
sns.barplot(data = oldAge, x='job', y='balance')
plt.show()

# Create a Line plot using Seaborn
sns.lineplot(data=df,x='job',y='age')
plt.show()

# Create a Bar plot
pd.crosstab(df.age,df.Target).plot(kind='bar')
plt.show()

# Create a Count plot using Seaborn
sns.countplot(data=df,x='marital')
plt.show()

# Split data into X (age) and y (balance)
x = df[['age']]
y = df['balance']


x_train, x_test,y_train, y_test= train_test_split(x, y, train_size = 0.3)
print(x_train.head())
print(x_test.head())

lr = LinearRegression()
lr.fit(x_train, y_train)
y_predict = lr.predict(x_test)
print(y_test.head())
print(y_predict[:5])


#  Find mean value using prediction and test value
mse = mean_squared_error(y_test,y_predict)
print(mse)

# Create a DataFrame to hold the actual and predicted balance data

record = pd.DataFrame({
    'Actual balance': y_test,
    'Predicted balance': y_predict
})

# Create a line plot using Seaborn
sns.lineplot(data = record)
plt.show()
