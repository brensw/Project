# Programming and Scripting Project 


## Dataset Used
The dataset used in this project is Fischer’s Iris data set. The data is taken from a 1936 paper by Ronald Fischer. The dataset conatains fifty instances of sepal length and width along with the petal length and width of three species of the Iris flowers, these being the Iris setosa, Iris virginica and Iris versicolor(UCI, n.d). 


## The Code and Analysis

The analysis of the dataset is carried out with the use of various Python libaries, the libaries required are imported in the first portion of code. The libaries used are:
* Pandas
* Numpy
* Seaborn
* Matplotlib
* Sklearn 

Once these libraries are imported, the dataset itself is loaded directly from the UCI archive URL, loading the dataset directly from the URL allows the code to be run on any machine with an internet connection, however, if any modification to the dataset was expected then loading from a locally stored copy fo the dataset would be preferable to ensure that any changes made previouly would be accessable. 

The dataset itself is in the CSV format, the Pandas library CSV tools are used to handle this file. The column are given appriate names and a dataframe created to allow for easier analysis. 

With the dataset loaded and formatted, the program creates a onscreen menu for the user giving user six options:
1. Display the data 
2. Display a summary of the data 
3. Create and show a scatter matrix of sepal vs petal length
4. Create and show a scatter matrix of of all varibles 
5. Display a graph displaying the realtive importance of each varible in determing the species of Iris
6. Exit the program.

The menu is intedned to reappear after an option other then Exit  has been selected to allow the user to carry out as many operations as desisred until they exit tje program. The menu itself is created using an 'if' loop, enter values from 1 to 6 causing the appropriate code to run, value higher then 6 causes an new message to enter a number between 1 and 6  to be displayed. 

If option one is selected then the Pandas dataframe created earlier is displayed to the user. 

If option two is selected 


## References
Jason Borwnlee 2016, Machine Learning Mastery, accessed on 22 April 2018,
<https://machinelearningmastery.com/machine-learning-in-python-step-by-step>.

Kaggle n.d., accessed on 22 April 2018, 
<https://www.kaggle.com/camontanezp/learning-python-data-analysis-with-iris>.

Micheal Waskom n.d., seaborn: statistical data visualization, accessed on 22 April 2018,
<https://seaborn.pydata.org/generated/seaborn.pairplot.html>.

https://www.python.org/

https://stackoverflow.com/questions/tagged/python

Fergus boyles 2017, Oxford Protein Informatics Group, accessed on 22 April 2018, 
<http://www.blopig.com/blog/2017/07/using-random-forests-in-python-with-scikit-learn/>.

https://ugoproto.github.io/ugo_py_doc/Exploratory%20Data%20Analysis/

UCI n.d., Universtiy California Irvine, Machine Learning Repository, accessed on 22 April 2018, <https://archive.ics.uci.edu/ml/datasets/iris>