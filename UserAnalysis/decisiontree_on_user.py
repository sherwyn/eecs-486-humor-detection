import json, os, sys
from sklearn import tree
import sexmachine.detector as gender
reload(sys)
sys.setdefaultencoding('utf-8')
'''
to run: python decisiontree_on_user.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>

output 2d matrix of [n_samples, n_features] for user profile
X: [[review_ct, num_friends, num_fans, elite, avg_star, gender],[...]]

 and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]

'''

def getUserMatrix(users):
    X = []
    Y = []
    d = sexmachine.detector.Detector(case_sensitive=False)
    for u in users:
        assert type(u) == dict
        male, female, andy = 0,0,0
        if d.get_gender(u["name"]) == "male":
            male = 1
        elif d.get_gender(u["name"]) == "female":
            female = 1
        elif d.get_gender(u["name"]) == "andy":
            andy = 1
        if male + female + andy == 1:
            entry = [int(u["review_count"]), len(u["friends"]), len(u["fans"]), male, female, andy, ]
            X.append(entry)

    for i in range(len(users)):
        Y.append("funny")
    return X, Y


def trainDecisionTree(funny_train, nonfunny_train):
    with open(funny_train, 'r') as f:
        json_str = f.read()
    funny_users = json.loads(json_str)

    with open(nonfunny_train, 'r') as f:
        json_str = f.read()
    nonfunny_users = json.loads(json_str)

    X, Y = getUserMatrix(funny_users + nonfunny_users)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf, funny_test, nonfunny_test):
    with open(funny_test, 'r') as f:
        json_str = f.read()
    funny_users = json.loads(json_str)

    with open(nonfunny_test, 'r') as f:
        json_str = f.read()
    nonfunny_users = json.loads(json_str)

    testX = []
    testY = []
    
    testX, testY = getUserMatrix(funny_users)
    # testX, testY = getUserMatrix(funny_users + nonfunny_users)

    # run decision tree on testdata
    print clf.predict(testX)


def main(funny_train, nonfunny_train, funny_test, nonfunny_test):
    clf = trainDecisionTree(funny_train, nonfunny_train)
    predictions = testDecisionTree(clf, funny_test, nonfunny_test)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

