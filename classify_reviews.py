# http://zacstewart.com/2015/04/28/document-classification-with-scikit-learn.html

import os
import io
import json
import numpy
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

def build_data_frame(path, classification):
    rows = []
    index = []

    with open(path) as json_data:
        d = json.load(json_data)
        for review in d:
            file_name = review['review_id']
            text = review['text']

            rows.append({'text': text, 'class': classification})
            index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame

# Loading Examples

FUNNY = 'funny'
NONFUNNY = 'nonfunny'

SOURCES = [
    ('data/yelp_funny_a.json',        FUNNY),
    ('data/yelp_nonfunny_a.json',    NONFUNNY),
    # ('data/yelp_funny_b.json',        FUNNY),
    # ('data/yelp_nonfunny_b.json',    NONFUNNY),
]

data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))

data = data.reindex(numpy.random.permutation(data.index))

# Pipelining

# SOURCES_TEST = [
#     ('data/yelp_funny_a.json',        FUNNY),
#     ('data/yelp_nonfunny_a.json',    NONFUNNY),
#     ('data/yelp_funny_b.json',        FUNNY),
#     ('data/yelp_nonfunny_b.json',    NONFUNNY),
# ]

# for path, classification in SOURCES_TEST:
#     with open(path) as json_data:
#         d = json.load(json_data)
#         examples = [x['text'] for x in d]

pipeline = Pipeline([
    ('vectorizer',  CountVectorizer()),
    ('classifier',  MultinomialNB()) ])

pipeline.fit(data['text'].values, data['class'].values)

# prediction_results = pipeline.predict(examples)
# print sum(x == FUNNY for x in prediction_results) / float(len(prediction_results))
# print sum(x == NONFUNNY for x in prediction_results) / float(len(prediction_results))

# Cross-Validating

k_fold = KFold(n=len(data), n_folds=6)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indices, test_indices in k_fold:
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values

    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=FUNNY)
    scores.append(score)

print 'Total reviews classified:', len(data)
print 'Score:', sum(scores)/len(scores)
print 'Confusion matrix:'
print confusion
