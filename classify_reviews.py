# EECS 486 Final Project
# Yelp Review Humor Detection
# Sherwyn Poon, Yidan Liu, Dennis Chang, Hannah Kim
# To run: python classify_reviews.py

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
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def get_dataframe(path, classification):
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

# Cross validating
def cross_validate(data, pipeline):
    k_fold = KFold(n=len(data), n_folds=6)
    scores = []
    confusion = numpy.array([[0, 0], [0, 0]])

    num_funny = 0
    num_nonfunny = 0

    for train_indices, test_indices in k_fold:
        train_text = data.iloc[train_indices]['text'].values
        train_y = data.iloc[train_indices]['class'].values

        test_text = data.iloc[test_indices]['text'].values
        test_y = data.iloc[test_indices]['class'].values

        pipeline.fit(train_text, train_y)
        predictions = pipeline.predict(test_text)

        num_funny += sum(p == FUNNY for p in predictions)
        num_nonfunny += sum(p == NONFUNNY for p in predictions)

        confusion += confusion_matrix(test_y, predictions)
        score = f1_score(test_y, predictions, pos_label=FUNNY)
        scores.append(score)

    return num_funny, num_nonfunny, scores, confusion

# Bag of words counts
def bag_of_words():
    return Pipeline([
        ('vectorizer',  CountVectorizer()),
        ('classifier',  MultinomialNB()) ])

# Bigram counts
def bigram_counts():
    return Pipeline([
        ('count_vectorizer', CountVectorizer(ngram_range=(1, 2))),
        ('classifier',       MultinomialNB())
    ])

# Bigram frequencies
def bigram_frequencies():
    return Pipeline([
        ('count_vectorizer',   CountVectorizer(ngram_range=(1,  2))),
        ('tfidf_transformer',  TfidfTransformer()),
        ('classifier',         MultinomialNB())
    ])

# Bigram occurences
def bigram_occurences():
    return Pipeline([
        ('count_vectorizer',   CountVectorizer(ngram_range=(1, 2))),
        ('classifier',         BernoulliNB(binarize=0.0)) ])

# Linear SVM
def linear_svm():
    return Pipeline([('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2',
        alpha=1e-3, n_iter=5, random_state=42))])

def print_results(num_funny, num_nonfunny, data, scores, confusion):
    print num_funny
    print num_nonfunny

    print 'Total reviews classified:', len(data)
    print 'F1 score:', sum(scores)/len(scores)
    print 'Confusion matrix:'
    print confusion

# Loading data

FUNNY = 'funny'
NONFUNNY = 'nonfunny'

SOURCES = [
    ('data/yelp_funny_a.json',        FUNNY),
    ('data/yelp_nonfunny_a.json',    NONFUNNY),
    ('data/yelp_funny_b.json',        FUNNY),
    ('data/yelp_nonfunny_b.json',    NONFUNNY),
]

data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(get_dataframe(path, classification))

data = data.reindex(numpy.random.permutation(data.index))

print 'MultinomialNB Bag of words'
pipeline = bag_of_words()
num_funny, num_nonfunny, scores, confusion = cross_validate(data, pipeline)
print_results(num_funny, num_nonfunny, data, scores, confusion)
print

print 'MultinomialNB Bigram counts'
pipeline = bigram_counts()
num_funny, num_nonfunny, scores, confusion = cross_validate(data, pipeline)
print_results(num_funny, num_nonfunny, data, scores, confusion)
print

print 'MultinomialNB Bigram frequencies'
pipeline = bigram_frequencies()
num_funny, num_nonfunny, scores, confusion = cross_validate(data, pipeline)
print_results(num_funny, num_nonfunny, data, scores, confusion)
print

print 'BernoulliNB Bigram occurences'
pipeline = bigram_occurences()
num_funny, num_nonfunny, scores, confusion = cross_validate(data, pipeline)
print_results(num_funny, num_nonfunny, data, scores, confusion)
print

print 'Linear SVM'
pipeline = linear_svm()
num_funny, num_nonfunny, scores, confusion = cross_validate(data, pipeline)
print_results(num_funny, num_nonfunny, data, scores, confusion)
print
