# EECS 486 Yelp Humor Detection

## Team members

  - Dennis Chang
  - Hannah Kim
  - Yidan Liu
  - Sherwyn Poon

## Datasets included

This repository contains the following datasets sourced from the Yelp Dataset Challenge: https://www.yelp.com/dataset_challenge

#### data/yelp_funny_a/b.json, data/yelp_nonfunny_a/b.json
Subsets of Yelp reviews from the set of all reviews, taken from Yelp Dataset challenge. Funny subsets (data/yelp_funny_a/b.json) contain only reviews with "funny" values of 3 or more. Non funny subsets (data/yelp_nonfunny_a/b.json) contain only reviews with "funny" values of 2 or less.

Data structure:
```sh
{
    "review_id":"encrypted review id",
    "user_id":"encrypted user id",
    "business_id":"encrypted business id",
    "stars":star rating, rounded to half-stars,
    "date":"date formatted like 2009-12-19",
    "text":"review text",
    "useful":number of useful votes received,
    "funny":number of funny votes received,
    "cool": number of cool review votes received,
    "type": "review"
}
```

#### BizAnalysis/yelp_funny_a/b_bizs.json, BizAnalysis/yelp_nonfunny_a/b_bizs.json
Subset of Yelp businesses from the set of all businesses, taken from Yelp Dataset Challenge.

Data structure:
```sh
{
    "business_id":"encrypted business id",
    "name":"business name",
    "neighborhood":"hood name",
    "address":"full address",
    "city":"city",
    "state":"state -- if applicable --",
    "postal code":"postal code",
    "latitude":latitude,
    "longitude":longitude,
    "stars":star rating, rounded to half-stars,
    "review_count":number of reviews,
    "is_open":0/1 (closed/open),
    "attributes":["an array of strings: each array element is an attribute"],
    "categories":["an array of strings of business categories"],
    "hours":["an array of strings of business hours"],
    "type": "business"
}
```

#### UserAnalysis/yelp_funny_a/b_users.json, UserAnalysis/yelp_nonfunny_a/b_users.json
Subset of Yelp users from the set of all users, taken from Yelp Dataset Challenge.

Data structure:
```sh
{
    "user_id":"encrypted user id",
    "name":"first name",
    "review_count":number of reviews,
    "yelping_since": date formatted like "2009-12-19",
    "friends":["an array of encrypted ids of friends"],
    "useful":"number of useful votes sent by the user",
    "funny":"number of funny votes sent by the user",
    "cool":"number of cool votes sent by the user",
    "fans":"number of fans the user has",
    "elite":["an array of years the user was elite"],
    "average_stars":floating point average like 4.31,
    "compliment_hot":number of hot compliments received by the user,
    "compliment_more":number of more compliments received by the user,
    "compliment_profile": number of profile compliments received by the user,
    "compliment_cute": number of cute compliments received by the user,
    "compliment_list": number of list compliments received by the user,
    "compliment_note": number of note compliments received by the user,
    "compliment_plain": number of plain compliments received by the user,
    "compliment_cool": number of cool compliments received by the user,
    "compliment_funny": number of funny compliments received by the user,
    "compliment_writer": number of writer compliments received by the user,
    "compliment_photos": number of photo compliments received by the user,
    "type":"user"
}
```

## Programs included

This repository contains the following programs used in our project:

#### Libraries
Required libraries can be installed using:

```sh
$ pip install -r requirements.txt
```

#### classify_reviews.py

This program runs the following 5 text classification models on our dataset:

* MultinomialNB Bag of words
* MultinomialNB Bigram counts
* MultinomialNB Bigram frequencies
* BernoulliNB Bigram occurences
* Linear SVM

Output: Prints the result of 5 text classification models on our Yelp review set.

```sh
$ python classify_reviews.py
```

#### get_user_biz_from_reviews.py

This program generates files needed for the next two programs to run. The datasets are too large for us to include in this repository, but can be downloaded at https://www.yelp.com/dataset_challenge. We've included the output of this program in /BizAnalysis and /UserAnalysis

Output: funny_filename_users.json, nonfunny_filename_users.json, funny_filename_bizs.json, nonfunny_filename_bizs.json

```sh
$ python get_user_biz_from_reviews.py data/yelp_funny_a.json data/yelp_nonfunny_a.json
$ python get_user_biz_from_reviews.py data/yelp_funny_b.json data/yelp_nonfunny_b.json
```

#### BizAnalysis/decisiontree_on_biz.py

This program trains a decision tree classifier with 2 sets of training data (1 funny and 1 nonfunny), and runs the generated decision tree classifier on test data.

It then prints the predicted labels for each review in test file, compares it with the given labels and computes the accuracy rate.

A PDF of the decision tree graph will also be generated (requires graphviz http://www.graphviz.org/). We've included the output graph in BizAnalysis/2000.pdf.

```sh
$ python BizAnalysis/decisiontree_on_biz.py BizAnalysis/yelp_funny_a_bizs.json BizAnalysis/yelp_nonfunny_a_bizs.json BizAnalysis/yelp_funny_b_bizs.json BizAnalysis/yelp_nonfunny_a_bizs.json
```

#### UserAnalysis/decisiontree_on_user.py

This program trains a decision tree classifier with 2 sets of training data (1 funny and 1 nonfunny), and runs the generated decision tree classifier on test data.

It then prints the predicted labels for each review in test file, compares it with the given labels and computes the accuracy rate.

A PDF of the decision tree graph will also be generated (requires graphviz http://www.graphviz.org/). We've included the output graph in UserAnalysis/2000.pdf.

```sh
$ python UserAnalysis/decisiontree_on_user.py UserAnalysis/yelp_funny_a_users.json UserAnalysis/yelp_nonfunny_a_users.json UserAnalysis/yelp_funny_b_users.json UserAnalysis/yelp_nonfunny_a_users.json
```
