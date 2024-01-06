Streamlit app link for flight price prediction:- https://flight-price-prediction-kzcqui9b8apprcybnfxfx6z.streamlit.app/
* Overview:-
- A Streamlit app for predicting flight ticket price is deployed with the help of Machine Learning and Python programming language
- This app makes things easy when planning to travel
  
* Data Collection:- 
- Source --> https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
- The dataset used in this project is taken from the above mentioned Kaggle link.
- Features such as airline names, places, duration of travel and classes (Economy and Business) are present in the dataset which helps in predicting the ticket price, where price is the target value.
- This prediction made is around 98% accurate, and the data used is based on similar websites

* Data Preprocessing:-
- The dataset is read using the Pandas library from a csv file and then looked for its dimensions, each columns' data types.
- Also, checked for the presence of any null values or duplicates

* Exploratory Data Analysis:-
- With the help of Seaborn and Matplotlib, many charts and graphs were plotted
- This step is crucial as it helps in visualizing differnet relationships between each feature present in the dataset
  
* Feature Engineering:-
Outlier removal:
- Using boxplot, outliers were found and removed, in order to obtain a clean data
One hot encoding:
- As, there are multi columns with categorical variables, label encoding was used, through which the data was ready for undergoing model buliding process

* Model Building and evaluation:-
- The data was separated into features and target followed by train test split
- As the target value is price, which is a continous variable, algorithms like Linear Regression, KNeighborsRegression and Random Forest Regression were used
- Grid Search CV method was employed in order to find the best model parameters

* Saving the model:- 
