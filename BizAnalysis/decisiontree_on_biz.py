import json, os, sys
from sklearn import tree
reload(sys)
sys.setdefaultencoding('utf-8')
'''
to run: python decisiontree_on_biz.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>

output 2d matrix of [n_samples, n_features] for businesses
X: [[review_ct, avg_star, UK, US, Germany, Canada],
 [review_ct, avg_star, UK, US, Germany, Canada] ]

 and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]

'''
def getBizMatrix(bizs):
    X = []
    Y = []

    for fb in bizs:
        assert type(fb) == dict
        entry = [int(fb["review_count"]), float(fb["stars"])]
        X.append(entry)
    for i in range(len(bizs)):
        Y.append("funny")
    return X, Y

def trainDecisionTree(funny_train, nonfunny_train):
    with open(funny_train, 'r') as f:
        json_str = f.read()
    funny_biz = json.loads(json_str)
    assert type(funny_biz) == list

    with open(nonfunny_train, 'r') as f:
        json_str = f.read()
    nonfunny_biz = json.loads(json_str)

    X, Y = getBizMatrix(funny_biz + nonfunny_biz)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf, funny_test, nonfunny_test):
    # convert test_data to matrix
    with open(funny_test, 'r') as f:
        json_str = f.read()
    funny_biz = json.loads(json_str)

    with open(nonfunny_test, 'r') as f:
        json_str = f.read()
    nonfunny_biz = json.loads(json_str)

    testX, testY = getBizMatrix(funny_biz)
    # testX, testY = getBizMatrix(funny_biz + nonfunny_biz)

    # run decision tree on testdata
    return clf.predict(testX)

def main(funny_train, nonfunny_train, funny_test, nonfunny_test):
    clf = trainDecisionTree(funny_train, nonfunny_train)
    predictions = testDecisionTree(clf, funny_test, nonfunny_test)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

