import json, os, sys, pydotplus
from sklearn import tree
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')
'''
to run: python decisiontree_on_biz.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>

Program prints predicted labels for test file, and accuracy rate.
Output decision tree graph in pdf


X: [[review_ct, avg_star],
 [review_ct, avg_star] ]

and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]

'''
def getBizMatrix(funny_train, nonfunny_train):
    with open(funny_train, 'r') as f:
        json_str = f.read()
    funny_biz = json.loads(json_str)
    assert type(funny_biz) == list

    with open(nonfunny_train, 'r') as f:
        json_str = f.read()
    nonfunny_biz = json.loads(json_str)

    X = []
    Y = []

    for fb in funny_biz:
        entry = [int(fb["review_count"]), float(fb["stars"])]
        X.append(entry)
    for i in range(len(funny_biz)):
        Y.append("funny")

    for fb in nonfunny_biz:
        entry = [int(fb["review_count"]), float(fb["stars"])]
        X.append(entry)
    for i in range(len(nonfunny_biz)):
        Y.append("nonfunny")

    return X, Y

def trainDecisionTree(funny_train, nonfunny_train):
    X, Y = getBizMatrix(funny_train, nonfunny_train)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf, funny_test, nonfunny_test):
    testX, testY = getBizMatrix(funny_test, nonfunny_test)

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
    testDecisionTree(clf, funny_test, nonfunny_test)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

