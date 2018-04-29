#Brendan Sweeney, 24/03/2018
#Iris dataset analysis

#Load libraries 
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns




# Load dataset (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pandas.read_csv(url, names=names) #downlaod iris csv file and add colunm names as dataset
df = pandas.DataFrame(dataset) # create pandas data frame with iris dataset

ex= 0
while ex == 0: #create loop to display option menu after chosen step is completed
    print ("Please enter an option")
    print ("To display dataset enter: 1")
    print ("To see a summary of the data enter: 2 ")
    print ("To create a scatter plot of petal length vs sepal length enter: 3")
    print("To create a scatter matirx for all varibles enter: 4")
    print ('To see relative importance of each varible enter: 5')
    print ("To exit enter: 6")

    n_in= int(input("Please enter the number of your choice:") )
    if n_in >= 7:
        print ("Please enter a number between 1 and 6")

    elif n_in == 6: # exit application
        raise SystemExit()

    elif n_in == 1: #display the dataset (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
        print(df)
        
    elif n_in == 2: #show basic analysis of dataset (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
        print(df.describe())

    elif n_in == 3: #create colour scatter plot sepal v petal length (https://www.kaggle.com/camontanezp/learning-python-data-analysis-with-iris)
        ax = dataset[dataset.species == "Iris-setosa"].plot(kind="scatter", x="sepal-length", y="petal-length", 
        color="red", label="Iris-setosa",title="Sepal Length vs. Petal Length")
        dataset[dataset.species == "Iris-virginica"].plot(kind="scatter", x="sepal-length", y="petal-length", 
        color="green", label="Iris-virginica", ax=ax)
        dataset[dataset.species == "Iris-versicolor"].plot(kind="scatter", x="sepal-length", y="petal-length", 
        color="blue", label="Iris-versicolor", ax=ax)
        plt.show()

    elif n_in == 4:
        sns.pairplot(df, hue='species',palette="husl",markers=["o", "s", "D"]) #create scatter matrix (https://seaborn.pydata.org/generated/seaborn.pairplot.html)
        plt.show()
        
    elif n_in == 5: #https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python
        X = dataset.iloc[:,0:4] # x varible values
        Y = dataset.iloc[:,-1] # y is species names
        names = dataset.columns.values
        rfc = RandomForestClassifier() 
        rfc.fit(X, Y)
        importance = rfc.feature_importances_
        sorted_importances = np.argsort(importance) #sort order big to small 
        padding = np.arange(len(names)-1) + 0.5  # line 65 to 70 format and show plot
        plt.barh(padding,importance[sorted_importances], color='g', align='center') 
        plt.yticks(padding, names[sorted_importances])
        plt.xlabel("Relative Importance")
        plt.title("Variable Importance")
        plt.show()



        






