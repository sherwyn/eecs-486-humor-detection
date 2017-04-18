# EECS 486 Yelp Humor Detection
## Team members
  - Dennis Chang
  - Hannah Kim
  - Yidan Liu
  - Sherwyn Poon

## Programs included

This repository contains the following programs used in our project:

#### classify_reviews.py
Output: Prints the result of 5 text classification models on our Yelp review set.
```sh
$ python classify_reviews.py
```
#### get_user_biz_from_reviews.py
Output: funny_filename_users.json, nonfunny_filename_users.json, funny_filename_bizs.json, nonfunny_filename_bizs.json
```sh
$ python get_user_biz_from_reviews.py <funny_filename> <nonfunny_filename>
```
#### BizAnalysis/decisiontree_on_biz.py
Output: 2d matrix of [n_samples, n_features] for businesses
X: [[review_ct, avg_star, UK, US, Germany, Canada],
 [review_ct, avg_star, UK, US, Germany, Canada] ]
and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]
```sh
$ python decisiontree_on_biz.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>
```
#### UserAnalysis/decisiontree_on_user.py
Output: 2d matrix of [n_samples, n_features] for user profile
X: [[review_ct, num_friends, num_fans, elite, avg_star, gender],[...]]
and list of labels:
Y: [funny, nonfunny, funny, nonfunny......]
```sh
$ python decisiontree_on_user.py <funny_train> <nonfunny_train> <funny_test> <nonfunny_test>
```
