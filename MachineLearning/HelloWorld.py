# from sklearn import tree
# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = ["Apple", "Apple", "Uday", "Pranav"]
# clf = tree.DecisionTreeClassifier().fit(features, labels)
# print clf.predict([[190,0]])
#
import urllib

link = "https://www.initialyze.com/"
f = urllib.urlopen(link)
myfile = f.read()
print myfile
