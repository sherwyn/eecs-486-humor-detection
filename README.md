# EECS 486 Yelp Humor Detection
## Team members
  - Dennis Chang
  - Hannah Kim
  - Yidan Liu
  - Sherwyn Poon

## Datasets included

This repository contains datasets sourced from the Yelp Dataset Challenge: https://www.yelp.com/dataset_challenge. One program, get_user_biz_from_reviews.py, requires yelp_academic_dataset_user.json and yelp_academic_dataset_business.json, files too large for us to include in this repository (but available in the link).

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
$ python get_user_biz_from_reviews.py yelp_funny_a.json yelp_nonfunny_a.json
$ python get_user_biz_from_reviews.py yelp_funny_b.json yelp_nonfunny_b.json
```
#### BizAnalysis/decisiontree_on_biz.py
Program prints predicted labels for test file, and accuracy rate.
Output decision tree graph in pdf
```sh
$ python decisiontree_on_biz.py yelp_funny_a_bizs.json yelp_nonfunny_a_bizs.json yelp_funny_b_bizs.json yelp_nonfunny_a_bizs.json
```
#### UserAnalysis/decisiontree_on_user.py
Program prints predicted labels for test file, and accuracy rate.
Output decision tree graph in pdf
```sh
$ python decisiontree_on_user.py yelp_funny_a_users.json yelp_nonfunny_a_users.json yelp_funny_b_users.json yelp_nonfunny_a_users.json
```
