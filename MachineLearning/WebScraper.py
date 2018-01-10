import urllib2
from bs4 import BeautifulSoup
from sklearn import tree

# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = ["Apple", "Apple", "Uday", "Uday"]
# clf = tree.DecisionTreeClassifier().fit(features, labels)
# print clf.predict([[190, 0]])

features = [['ctl00_PlaceHolderMain_EditModePanel2', 'Solution'], ['ctl00_PlaceHolderMain_EditModePanel2', 'Answer'],
            ['ctl00_PlaceHolderMain_EditModePanel2', 'Problem Description']]
labels = ['HowTo', 'FAQ', 'Solution']

clf = tree.DecisionTreeClassifier()
print clf
clf = clf.fit(features, labels)

print clf.predict([['ctl00_PlaceHolderMain_EditModePanel2', 'Solution']])


quote_page = ["https://kb.informatica.com/howto/6/Pages/1/152445.aspx",
              "https://kb.informatica.com/howto/6/Pages/_0/160073.aspx",
              "https://kb.informatica.com/faq/7/Pages/12/270781.aspx",
              "https://kb.informatica.com/howto/6/Pages/19/503582.aspx",
              "https://kb.informatica.com/solution/23/Pages/57/497429.aspx",
              "https://network.informatica.com/videos/2264",
              "https://kb.informatica.com/solution/23/Pages/57/495934.aspx",
              "https://kb.informatica.com/solution/19/Pages/124454.aspx",
              "https://kb.informatica.com/howto/6/Pages/1/152445.aspx"]

for url in quote_page:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find(attrs={'id': 'ctl00_PlaceHolderMain_EditModePanel2'})
    name = name_box.text.strip()
    print 'namebox ' + name_box
    print 'name = ' + name
