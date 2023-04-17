import numpy as np
import pandas as pd

import os
os.chdir("C:/Users/User/PycharmProjects/BevAdat/HAZI/HAZI06")

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#from src.DecisionTreeClassifier import DecisionTreeClassifier
from NJCleaner import NJCleaner
from DecisionTreeClassifier import DecisionTreeClassifier


njc = NJCleaner("2018_03.csv")
hfdata = njc.prep_df()

X = hfdata.iloc[:,:-1].values
Y = hfdata.iloc[:,-1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)

#classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=4)
#classifier.fit(X_train, Y_train)

#Y_pred = classifier.predict(X_test)
#print(accuracy_score(Y_test, Y_pred))
#classifier.print_tree()

def grid_search(data):
    X = hfdata.iloc[:,:-1].values
    Y = hfdata.iloc[:,-1].values.reshape(-1,1)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)
    classifier = DecisionTreeClassifier(min_samples_split=1,max_depth=1)
    accuracies = []

    for i in range(1,20,2):
        for j in range(3, 5):
            classifier.__init__(min_samples_split=i,max_depth=j)
            classifier.fit(X_train, Y_train)
            Y_pred = classifier.predict(X_test)
            accuracy = {}
            accuracy["min_samples_split"] = i
            accuracy["max_depth"] = j
            accuracy["accuracy"] = accuracy_score(Y_test, Y_pred)
            accuracies.append(accuracy)

    return accuracies


print("started")
acc = grid_search(hfdata)
print("done")
print(acc)

#Elég lassan futnak le a fitelések, gondolom a rekurzió meg a nagy adatmennyiség miatt. Megírtam a gridsearchot és hagytam dolgozni.
# Nagy szórást nem vettem észre az eredmények között: 79% szitne mindig, még az is beválik neki, ha mindenre 0-t mond. Apró javulások akkor vettem észre, ha a min_samples_split-et feljebb vettem. Ha a max_depth 6 vagy annál nagyobb, akkor egy üres best_split miatt el crashel.

#min_samples_split=20, max_depth=5 -> 0.7954779245360655
#min_samples_split=5, max_depth=5 -> 0.7954779245360655
#min_samples_split=50, max_depth=3 -> 0.7956013660864913
#min_samples_split=100, max_depth=4 -> 0.7955396453112784
#min_samples_split=0, max_depth=5 -> 0.7954779245360655
#'min_samples_split': 19, 'max_depth': 4, 'accuracy': 0.7955396453112784
#'min_samples_split': 1, 'max_depth': 3, 'accuracy': 0.7956013660864913 
#'min_samples_split': 11, 'max_depth': 4, 'accuracy': 0.7955396453112784 
#'min_samples_split': 3, 'max_depth': 4, 'accuracy': 0.7955396453112784
#'min_samples_split': 3, 'max_depth': 3, 'accuracy': 0.7956013660864913