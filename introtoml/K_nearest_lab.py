import numpy 
import matplotlib.pyplot as plt
import pandas 
import numpy 
from sklearn import preprocessing

data= pandas.read_csv('teleCust1000t.csv')


""" #We can print these to get a better grasp of our data
print(data.head(10))  
print(data.describe())
print(data['custcat'].value_counts()) 
"""

#print(data.columns)
#to use the sklearn library we have to convert the pandas data frame to numpy array:
x= data[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed','employ', 'retire', 'gender', 'reside', 'custcat']].values 
#print(x[0:5]) 
y= data['custcat'].values
#print(y[0:5])  #this prints the custcat for the first 5 items


#Data Standardization gives the data zero mean and unit variance, it is good practice, especially for algorithms such as KNN which is based on the distance of data points
x = preprocessing.StandardScaler().fit(x).transform(x.astype(float))
#print(x[0:5])


from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state= 4)


	#classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
"""
#training
k= 4
neigh= KNeighborsClassifier(n_neighbors= k).fit(x_train, y_train)

#predicting 
yhat= neigh.predict(x_test)

#evaluation
from sklearn import metrics

print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(x_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
"""
Ks = 10
mean_acc = numpy.zeros((Ks-1))
std_acc = numpy.zeros((Ks-1))

for n in range(1,Ks):
    
    #Train Model and Predict  
    neigh = KNeighborsClassifier(n_neighbors = n).fit(x_train,y_train)
    yhat=neigh.predict(x_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)

    
    std_acc[n-1]=numpy.std(yhat==y_test)/numpy.sqrt(yhat.shape[0])

#print(mean_acc)
print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1) 
