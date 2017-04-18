import json, os, sys, pydotplus
from sklearn import tree
import numpy as np
import gender_predictor.detector as gender
reload(sys)
sys.setdefaultencoding('utf-8')
'''
to run: python decisiontree_on_user.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>

Program prints predicted labels for test file, and accuracy rate.
Output decision tree graph in pdf



X: [[review_ct, num_friends, num_fans, elite, avg_star, gender],[...]]

 and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]

'''

def getUserMatrix(funny, nonfunny):
    with open(funny, 'r') as f:
        json_str = f.read()
    funny_users = json.loads(json_str)

    with open(nonfunny, 'r') as f:
        json_str = f.read()
    nonfunny_users = json.loads(json_str)

    X = []
    Y = []
    # d = gender.Detector(case_sensitive=False)

    for u in funny_users:
        elite = -1
        # male, female, andy, elite = -1, -1, -1, -1
        # if d.get_gender(u["name"]) == "male":
        #     male = 1
        # elif d.get_gender(u["name"]) == "female":
        #     female = 1
        # elif d.get_gender(u["name"]) == "andy":
        #     andy = 1
        # assert type(u["elite"]) == list
        if u["elite"][0] != "None":
            elite = 1
        # entry = [int(u["review_count"]), len(u["friends"]), int(u["fans"]), elite, float(u["average_stars"]), male, female, andy]
        entry = [int(u["review_count"]), len(u["friends"]), int(u["fans"]), elite]
        X.append(entry)

    for i in range(len(funny_users)):
        Y.append("funny")

    for u in nonfunny_users:
        elite = -1
        # male, female, andy, elite = -1, -1, -1, -1
        # if d.get_gender(u["name"]) == "male":
        #     male = 1
        # elif d.get_gender(u["name"]) == "female":
        #     female = 1
        # elif d.get_gender(u["name"]) == "andy":
        #     andy = 1
        if u["elite"][0] != "None":
            elite = 1
        # entry = [int(u["review_count"]), len(u["friends"]), int(u["fans"]), elite, float(u["average_stars"]), male, female, andy]
        entry = [int(u["review_count"]), len(u["friends"]), int(u["fans"]), elite]
        X.append(entry)

    for i in range(len(nonfunny_users)):
        Y.append("nonfunny")

    return X, Y


def trainDecisionTree(funny_train, nonfunny_train):
    X, Y = getUserMatrix(funny_train, nonfunny_train)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf, funny_test, nonfunny_test):
    testX, testY = getUserMatrix(funny_test, nonfunny_test)

    # run decision tree on testdata
    predictions = clf.predict(testX).tolist()
    print predictions

    num_correct = 0
    for i in range(len(predictions)):
        if predictions[i] == testY[i]:
            num_correct += 1

    accuracy = num_correct / float(len(predictions))
    print "accuracy is " + str(accuracy)

    # output graph
    dot_data = tree.export_graphviz(clf, out_file=None) 
    graph = pydotplus.graph_from_dot_data(dot_data) 
    graph.write_pdf("tree.pdf") 

def main(funny_train, nonfunny_train, funny_test, nonfunny_test):
    clf = trainDecisionTree(funny_train, nonfunny_train)
    predictions = testDecisionTree(clf, funny_test, nonfunny_test)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

