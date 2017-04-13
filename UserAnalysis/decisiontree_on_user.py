import json, os, sys
from sklearn import tree
import sexmachine.detector as gender
reload(sys)
sys.setdefaultencoding('utf-8')
'''
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


def trainDecisionTree():
    # with open('funny_users_a.json', 'r') as f:
    with open('funny_users_sm.json', 'r') as f:
        json_str = f.read()
    funny_users = json.loads(json_str)

    # with open('nonfunny_users_a.json', 'r') as f:
    with open('nonfunny_users_sm.json', 'r') as f:
        json_str = f.read()
    nonfunny_users = json.loads(json_str)

    X, Y = getUserMatrix(funny_users + nonfunny_users)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf):
    # convert test_data to matrix
    # with open('funny_users_b.json', 'r') as f:
    with open('funny_users_sm.json', 'r') as f:
        json_str = f.read()
    funny_users = json.loads(json_str)

    # with open('nonfunny_users_b.json', 'r') as f:
    with open('nonfunny_users_sm.json', 'r') as f:
        json_str = f.read()
    nonfunny_users = json.loads(json_str)

    testX = []
    testY = []
    
    testX, testY = getUserMatrix(funny_users)
    # testX, testY = getUserMatrix(funny_users + nonfunny_users)

    # run decision tree on testdata
    print clf.predict(testX)


def main():
    clf = trainDecisionTree()
    testDecisionTree(clf)

if __name__ == "__main__":
    main()

