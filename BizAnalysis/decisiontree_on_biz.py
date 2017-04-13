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
        entry = []
        entry.append(int(fb["review_count"]))
        entry.append(float(fb["stars"]))
        X.append(entry)
    for i in range(len(bizs)):
        Y.append("funny")
    return X, Y

def trainDecisionTree():
    # with open('funny_bizs_a.json', 'r') as f:
    with open('funny_bizs_sm.json', 'r') as f:
        json_str = f.read()
    funny_biz = json.loads(json_str)

    # with open('nonfunny_bizs_a.json', 'r') as f:
    with open('nonfunny_bizs_sm.json', 'r') as f:
        json_str = f.read()
    nonfunny_biz = json.loads(json_str)

    X, Y = getBizMatrix(funny_biz + nonfunny_biz)

    print X
    print Y

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)

    return clf

def testDecisionTree(clf):
    # convert test_data to matrix
    # with open('funny_bizs_b.json', 'r') as f:
    with open('funny_bizs_sm.json', 'r') as f:
        json_str = f.read()
    funny_biz = json.loads(json_str)

    testX, testY = getBizMatrix(funny_biz)

    # with open('nonfunny_bizs_b.json', 'r') as f:
    #     json_str = f.read()
    # nonfunny_biz_b = json.loads(json_str)

    # for nb in nonfunny_biz_b:
    #     x = [int(nb["review_count"]), float(nb["stars"])]
    #     testX.append(x)
    # for i in range(len(nonfunny_biz_b)):
    #     testY.append("nonfunny")

    # run decision tree on testdata
    return clf.predict(testX)

def main():
    clf = trainDecisionTree()
    predictions = testDecisionTree(clf)


if __name__ == "__main__":
    main()

