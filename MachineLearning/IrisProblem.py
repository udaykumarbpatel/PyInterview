import numpy as np
from sklearn.datasets import load_iris


class MYKClassifier():
    def fit(self, X_train, y_train):
        pass

    def predict(self, X_test):
        pass


iris = load_iris()

#
#*****feature name
# print iris.feature_names
#*****label name
# print iris.target_names
#*****Actual data
#print iris.data[0]
#*****Label for the data
# print iris.target[0]

X = iris.data
y = iris.target

# Split the dataset into two to train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# # Basic Classifier DECISIONTREE
# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

# # Neighbor Classifier
# from sklearn.neighbors import KNeighborsClassifier
# my_classifier = KNeighborsClassifier()

#Own Classifier
from sklearn.neighbors import KNeighborsClassifier
my_classifier = MYKClassifier()


my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)


from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)