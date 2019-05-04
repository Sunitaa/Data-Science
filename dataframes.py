#data frames
import pandas as pd
print (pd.__version__)

#connect to the database or read a file
titanic_train = pd.read_csv("C:/Data Science/Titanic_disaster/test.csv") 
print(type(titanic_train))

#prints number of rows and columns
titanic_train.shape #(891,12), header is not counted

#prints columns, data count, nullable, data type
titanic_train.info() 

#gives all the statistical information of each and every column
titanic_train.describe()


#access column/columns of a dataframe
titanic_train['Sex']
titanic_train['Fare']
titanic_train.Sex #same as titanic_train['Sex'] 
titanic_train.Fare

temp = titanic_train[['Age', 'Fare', 'Embarked']]
print(type(temp))

#access rows of a data frame
titanic_train.iloc[8] #9th record

titanic_train[10:20] 
titanic_train.iloc[10:20]

titanic_train[885:891]
titanic_train.iloc[885:891]

#Get me top 10 records
titanic_train.head(10)
#Get me bottom 10 records
titanic_train.tail(10)

#access both rows and columns of a dataframe
titanic_train.iloc[10:11]

#access by column name then use .loc
titanic_train.loc[10:20,('Name', 'Age')]

#conditional access of dataframe
titanic_train.loc[titanic_train.Sex == 'male', ('Sex', 'Age', 'Pclass', 'Name')]

#grouping data in data frames
titanic_train.groupby(['Embarked']).size()
titanic_train.groupby(['Pclass', 'Sex']).size()
titanic_train.groupby(['Embarked', 'Pclass']).mean()

titanic_train.groupby(['Embarked', 'Pclass']).mean()['Fare']
