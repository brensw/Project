#Brendan Sweeney, 24/03/2018
#Iris dataset analysis

#Load libraries (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier




# Load dataset (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pandas.read_csv(url, names=names)



print ("Please enter an option")
print ("To display dataset enter: 1")
print ("To see a summary of the data enter: 2 ")
print ("To create a scatter plot of petal length vs sepal length enter: 3")
print ('To see relative importance of each varible enter: 4')
print ("To exit enter: 5")

n_in= int(input("Please enter the number  of your choice:") )
if n_in >= 6:
    print ("Please enter a valid number")
elif n_in == 5: # exit application
    raise SystemExit()
elif n_in == 1: #display the dataset :https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
    print(dataset.head())
elif n_in == 2: #show basic analysis of dataset: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
    print(dataset.describe())
elif n_in == 3: #create colour scatter plot for each species:  https://www.kaggle.com/camontanezp/learning-python-data-analysis-with-iris
    ax = dataset[dataset.species == "Iris-setosa"].plot(kind="scatter", x="sepal-length", y="petal-length", 
    color="red", label="Iris-setosa",title="Sepal Lenght vs. Petal Length")
    dataset[dataset.species == "Iris-virginica"].plot(kind="scatter", x="sepal-length", y="petal-length", 
    color="green", label="Iris-virginica", ax=ax)
    dataset[dataset.species == "Iris-versicolor"].plot(kind="scatter", x="sepal-length", y="petal-length", 
    color="blue", label="Iris-versicolor", ax=ax)
    plt.show()
elif n_in == 4:
    X = dataset.iloc[:,0:4]
    Y = dataset.iloc[:,-1]
    names = dataset.columns.values
    rfc = RandomForestClassifier()
    rfc.fit(X, Y)
    importance = rfc.feature_importances_
    sorted_importances = np.argsort(importance)
    padding = np.arange(len(names)-1) + 0.5
    plt.barh(padding, importance[sorted_importances], align='center')
    plt.yticks(padding, names[sorted_importances])
    plt.xlabel("Relative Importance")
    plt.title("Variable Importance")
    plt.show()


        


raise SystemExit()



