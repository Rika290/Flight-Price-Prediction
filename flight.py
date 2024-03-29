# -*- coding: utf-8 -*-
"""Flight.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jCVfWPfFdP3xGsbSiXZwEffsfwmsoyAu

Data Source: https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""(1) **Data Loading**"""

flight_data=pd.read_csv('/content/drive/MyDrive/Clean_Dataset.csv')

# reading the 1st 3 rows of the dataset
flight_data.head(3)

"""As the column Unnmed: 0 is not needed, it is dropped"""

flight_data=flight_data.drop(columns=['Unnamed: 0'])

"""**Reading the dataset**"""

# reading the 1st 3 rows of the dataset
flight_data.head(3)

# reading the last 3 rows of the dataset
flight_data.tail(3)

"""(2) **Exploratory Data Analysis**

Dimensions of the dataset
"""

flight_data.shape

"""Checking the data types for each column"""

flight_data.dtypes

print('Null values:',flight_data.isnull().any().sum())
print('NaN values:', flight_data.isna().any().sum())
print('duplicates:',flight_data.duplicated().any().sum())

"""The dataset does not have any null, missing, duplicate  values

a. Checking for no.of distinct values in each column in the dataset
"""

flight_data.nunique()

"""b. No.of flights per class - Economy and Business"""

sns.set(font_scale=0.7)
cl={'Economy':'green','Business':'blue'}
c=sns.countplot(data=flight_data,x='class',palette=cl)
for label in c.containers:
  c.bar_label(label)

"""c. Total number of flights under each Airline and class"""

sns.set(font_scale=0.6)
plt.figure(figsize=(6,4))
col={'Economy':'red','Business':'green'}
a=sns.countplot(data=flight_data,x='airline',hue='class',palette=col)
for l in a.containers:
  a.bar_label(l)
plt.title('Flight counts per airline')
plt.xlabel('Airline')
plt.ylabel('Total number of flights')

"""1. Among the six airlines, only Vistara and Air India have both classes Economy and Business
2. And the airline Vistara has the highest no.of flights from both classes
3. Spicejet is the airline which has lowest no.of flights

d. Plotting No.of flights per cities and class category
"""

sns.set(font_scale=0.5) # setting the font scale
plt.figure(figsize=(10,8)) # setting the chart size

plt.subplot(1,2,1) # 1st plot in the subplot
col={'Economy':'purple','Business':'green'}
ax=sns.countplot(data=flight_data,x='source_city',hue='class',palette=col)
plt.title('No.of flights per source city')
plt.xlabel('Source Cities')
plt.ylabel('No.of flights')
for label in ax.containers:
    ax.bar_label(label) # adding label to the bars

plt.subplot(1,2,2) # 2nd plot in the sub plot
col={'Economy':'purple','Business':'green'}
bx=sns.countplot(data=flight_data,x='destination_city',hue='class',palette=col)
sns.move_legend(bx,"right")
plt.title('No.of flights per destination city')
plt.xlabel('Destination Cities')
plt.ylabel('No.of flights')
for c in bx.containers:
  bx.bar_label(c)
plt.show()

"""From both charts,
*  Economy class:- Delhi has the highest number, and
*  Business class:- Mumbai is the city with  highest no.of flights

e. Statistical info of the dataset
"""

flight_data.describe()

"""f. Viewing ticket price by each airline and class"""

flight_data[['airline','price','class']].sort_values(by='price',ascending=False)

"""Among the various airlines, Vistara charges highest price under the business class.

g. Ticket price vs class based on different airlines
"""

sns.set(font_scale=0.7)
plt.figure(figsize=(9,9))
x=sns.barplot(data=flight_data,x='class',y='price',hue='airline',errorbar=None)
for i in x.containers:
  x.bar_label(i)
plt.xlabel('Class')
plt.ylabel('Ticket Price')
plt.title('Flight ticket price vs class based on each airline')

"""The ticket price charged by Vistara is the highest under both classes, and AirAsia offers the lowest under Economy class.

h. Plotting No.of flights per class under different departure and arrival time.
"""

sns.set(font_scale=0.7)
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
cl=sns.countplot(data=flight_data,x='departure_time',hue='class')
for l in cl.containers:
  cl.bar_label(l)

plt.subplot(2,1,2)
cl=sns.countplot(data=flight_data,x='arrival_time',hue='class')
for l in cl.containers:
  cl.bar_label(l)

"""This graph shows that, more morning flights are departed as well as  more night flights arrive at the airport.

i. Analysing ticket price vs destination and source cities base on each class
"""

sns.set(font_scale=0.7)
plt.figure(figsize=(8,6))

plt.subplot(2,1,1)
cl=sns.barplot(data=flight_data,x='destination_city',y='price',hue='class')
for l in cl.containers:
  cl.bar_label(l)

plt.subplot(2,1,2)
cl=sns.barplot(data=flight_data,x='source_city',y='price',hue='class')
for l in cl.containers:
  cl.bar_label(l)

"""Kolkata's flight is the costliest

j. Analysing duration of flights
"""

flight_data['duration'].describe()

# Row numbers of flights with minimum duration
flight_data[flight_data['duration']== 49.830000].index

# Row numbers of flights with maximum duration
flight_data[flight_data['duration']== 0.830000].index

"""(4) Feature Engineering

1. Checking for outliers in price column
"""

sns.boxplot(data=flight_data,x='price')

"""From the boxplot, we can infer that, the flight ticket price falls in the range of 0 to 100000 only, whereas there are few outliers that is beyond the value of 120000. Since, the dataset is large enough, the outliers are removed from the data in order to develop a proper model for the prediction.


"""

f_out=flight_data[flight_data['price']>=100000].index
flight_data=flight_data.drop(index=f_out)

sns.boxplot(x=flight_data['price'])

flight_data.shape

flight_data[['destination_city','price']].groupby('destination_city').max()

flight_data[flight_data['price']==99680]

flight_data.head(2)

"""Vistara offers Business Class at the highest ticket price to the city Mumbai flies from Bangalore with duration of 14.42 at Rs 99680.

2. Removing unnecessary columns
"""

flight_data=flight_data.drop(columns='flight')

"""3. Encoded multi columns containing categorical varibles at once"""

from sklearn.preprocessing import LabelEncoder

df=flight_data.iloc[:,:7] # poisition of columns that have categorical variables

# Encoding:
enc_all_cols=df.apply(LabelEncoder().fit_transform)


#Concating with the remaining columns of the dataset
df_enc=pd.concat([enc_all_cols,flight_data.iloc[:,-3:]],axis=1)

# reading the first 2 rows of the dataframe which now has encoded data and ready for train test split
df_enc.head(2)

"""(5) Model Building

Train test split
"""

from sklearn.model_selection import train_test_split

X = df_enc.drop(columns='price') # feature
y=df_enc['price']  # target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
print('X_train size: {}, X_test size: {}'.format(X_train.shape, X_test.shape))
print('y_train size: {}, y_test size: {}'.format(y_train.shape, y_test.shape))

"""Finding the best model with the help of GridSearchCV"""

from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

model_params={
    'LR':{
        'model':LinearRegression(),
        'params':{

        }
    },
    'KNR':{
        'model':KNeighborsRegressor(),
        'params':{
            'n_neighbors':[2,5,10]
        }
    },
    'RFR':{
        'model':RandomForestRegressor(),
        'params':{
            'n_estimators':[5,10,20]
        }
    }
}

from sklearn.model_selection import ShuffleSplit
scores=[]
cv = ShuffleSplit(n_splits=5, test_size=0.20, random_state=0)
for model,mp in model_params.items():
  clf=GridSearchCV(mp['model'],mp['params'],cv=cv,return_train_score=False)
  clf.fit(X,y)
  scores.append({
      'model':model,
      'best score':clf.best_score_,
      'best params':clf.best_params_
  })

dd=pd.DataFrame(scores,columns=['model','best score','best params'])
dd

"""Among the 3 models used, Random Forest Regressor gives the highest score.

Hence, a model with the Random Forest Regression is built and evaluated.
"""

from sklearn.model_selection import cross_val_score
cv=ShuffleSplit(n_splits=5,test_size=0.2)
s=cross_val_score(RandomForestRegressor(n_estimators=20),X,y,cv=cv)
print('Average Accuracy : {}%'.format(round(sum(s)*100/len(s)), 3))

rf=RandomForestRegressor(n_estimators=20)

rf.fit(X_train,y_train)

r_pred=rf.predict(X_test)

"""evaluating the model"""

from sklearn import metrics
metrics.r2_score(r_pred,y_test)

"""Looking for the labels of the categorical columns- For reference (Since the columns are encoded)"""

print('AIRLINE')
print(flight_data['airline'].value_counts())
print(X['airline'].value_counts())
print('\n')
print('SOURCE CITY')
print(flight_data['source_city'].value_counts())
print(X['source_city'].value_counts())
print('\n')
print('DEPARTURE TIME')
print(flight_data['departure_time'].value_counts())
print(X['departure_time'].value_counts())

print('STOPS')
print(flight_data['stops'].value_counts())
print(X['stops'].value_counts())
print('\n')
print('ARRIVAL TIME')
print(flight_data['arrival_time'].value_counts())
print(X['arrival_time'].value_counts())
print('\n')
print('DESTINATION CITY')
print(flight_data['destination_city'].value_counts())
print(X['destination_city'].value_counts())
print('\n')
print('CLASS')
print(flight_data['class'].value_counts())
print(X['class'].value_counts())

flight_data.sample(1)

"""Testing the model with values"""

print('Price:',rf.predict([[5,5,5,0,4,3,0,12.75,35]])) # org= 64700   - X_train
print('Price:',rf.predict([[5,5,4,0,4,3,1,24.0,48]]))# org= 3334 - X_train
print('Price:',rf.predict([[2,0,5,0,4,2,1,9.67,34]]))# org = 3826 - X_test
print('Price:',rf.predict([[1,5,0,0,4,0,0,17.33,29]])) #org = 54608 X_test

"""As per the model evaluation, the prediction is around 99% accurate. Therefore, for flight prediction, 'rf' the model is chosen.

(6) Saving the model
"""

import pickle

flight_data.sample(1)

"""**"""

pickle_out1 = open("rfreg.pkl", "wb")
pickle.dump(rf, pickle_out1)
pickle_out1.close()

"""**"""

filename='trained_model.sav'
pickle.dump(rf,open(filename,'wb'))

"""Checking/loading the model"""

load=pickle.load(open('trained_model.sav','rb'))

load.predict([[5,5,4,0,4,3,1,24.0,48]])

