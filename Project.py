#Brendan Sweeney, 24/03/2018
#Iris dataset analysis

#Load libraries (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
dataset = pandas.read_csv(url, names=names)



print ("Please enter an option")
print ("To display dataset enter: 1")
print ("To see a summary of the data enter: 2 ")
print ("To create a scatter plot of petal length vs sepal length enter: 3")
print ("To exit enter: 4")
n_in= int(input("Please enter the number  of your choice:") )
if n_in >= 5:
    print ("Please enter a valid number")
elif n_in == 4: # exit application
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

raise SystemExit()



