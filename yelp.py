import json
from numpy import std, mean

in_file = 'yelp_academic_dataset_review.json'
# in_file = 'sample.json'
out_file = 'yelp_nonfunny_a.json'
with open(in_file, 'r+') as f_in, open(out_file, 'w+') as f_out:
    data = f_in.readlines()[50000:100000]
    data = [json.loads(x) for x in data]

    # As we proceed, we make an arbitrary assumption - a review is "funny" if
    # it obtains three or more funny votes.
    # filtered = [x for x in data if x['funny'] >= 3][:1000]
    filtered = [x for x in data if x['funny'] < 3][:1000]
    print len(filtered)

    f_out.write(json.dumps(filtered))
