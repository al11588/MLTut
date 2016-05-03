from sklearn import tree

cars = [[140, 1], [ 130, 1], [ 150, 0], [170, 0]]

people = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(cars, people)

print clf.predict([[ 150, 0]])