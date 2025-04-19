from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np


def get_iris_dataset():
    iris = datasets.load_iris()
    X, y = iris.data[:, [0, 1]], iris.target
    df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])
    return df

def perform_train_test_split():
    df = get_iris_dataset()
    """
    Perform a train/test split. Return a tuple in the format (X_train, X_test, Y_train, Y_test)
    
    Hint: Define your features and target 
    """
    #YOUR CODE HERE
    Y = df["target"]
    X = df.drop(["target"], axis=1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)
    return (X_train, X_test, Y_train, Y_test)

def instantiate_models():
    """
    Fill in the blanks to instantiate the models using scikit learn. Return a tuple in the format:
    (SVM model, Decision Tree model, MLP model, KNN Model)
    
    Fill in the blanks as shown
    """
    #YOUR CODE HERE
    svm = SVC(C=0.7)
    dt = DecisionTreeClassifier()
    mlp = MLPClassifier()
    knn = KNeighborsClassifier()
    return (svm, dt, mlp, knn)

def fit_models():
    """
    For each model from the instantiate_model() function, fit the models. 
    
    Fill in the blanks as ashown
    """
    svm, dt, mlp, knn = instantiate_models()
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    svm.fit(X_train, Y_train)
    dt.fit(X_train, Y_train)
    mlp.fit(X_train, Y_train)
    knn.fit(X_train, Y_train)
    return (svm, dt, mlp, knn) #return fitted models


def accuracy_at_least_90():
    """
    Choose a model from the instantiate_models function. Play around with the hyperparameters (eg: turning the dials and 
    knobs) from the instantiate_models() function and get the accuracy to at least 0.9.
    
    Recommended link to help you: https://scikit-learn.org/stable/supervised_learning.html
    
    The above link contains documentation to the scikit-learn library you are using
    
    Fill in the blanks
    """
    X_train, X_test, Y_train, Y_test = perform_train_test_split()
    
    svm, dt, mlp, knn = instantiate_models()
    
    model = svm #pick model and put it here
    
    model.fit(X_train, Y_train) #once you pick a model, what do you need to do to train it?
    
    pred = model.predict(X_test) #once you fit a model, how do you predict
    
    return (model, accuracy_score(Y_test, pred)) #Return tuple format (model, accuracy). Look at sklearn.metrics to see how to calculate accuracy
    
    
    
