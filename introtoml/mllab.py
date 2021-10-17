import matplotlib.pyplot as plt
import pandas 
import pylab
import numpy
from sklearn import linear_model

#reading the data in 
data= pandas.read_csv("FuelConsumption.csv")
#print(data.head())   #prints the head
#print(data.describe())   #describes the data

ddata= data[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']] #selects the important columns from the data
#print(ddata.head(10))

#We can plot each of these features
#ddata.hist()
#plt.show()

#now lets plot these features against the emission to see how linear it is
#plt.scatter(ddata.ENGINESIZE, ddata.CO2EMISSIONS, color= 'blue')
#plt.xlabel('ENGINESIZE')
#plt.ylabel('EMISSION')
#plt.show()


#Regression model

#Lets split the model into Model type Train/test split %80train %20 test
msk= numpy.random.rand(len(ddata)) < 0.8
train = ddata[msk]  #variable data might be wrong?? 
test = ddata[~msk]
"""
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color= 'blue')
plt.xlabel('ENGINESIZE')
plt.ylabel('EMISSION')
plt.show()
"""

#Using sklearn package to model data
regr= linear_model.LinearRegression()
train_x= numpy.asanyarray(train[['ENGINESIZE']])
train_y= numpy.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)
#print('Coefficents:', regr.coef_) 
#print('Intercept:', regr.intercept_)

"""
#plotting outputs
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
"""
#Evaluating result
from sklearn.metrics import r2_score

test_x = numpy.asanyarray(test[['ENGINESIZE']])
test_y = numpy.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)

print("Mean absolute error: %.2f" % numpy.mean(numpy.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % numpy.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y , test_y_) )



