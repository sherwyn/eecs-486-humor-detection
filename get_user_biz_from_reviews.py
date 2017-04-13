import json, os, sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
run: python get_user_biz_from_reviews.py <funny_filename> <nonfunny_filename>
creates funny_filename_users.json, nonfunny_filename_users.json, funny_filename_bizs.json, nonfunny_filename_bizs.json

'''

def get_user_biz_id(jdata):
    user_ids = []
    biz_ids = []
    # output list of user_ids & list of business_ids
    for review in jdata:
        user_ids.append(review["user_id"])
        biz_ids.append(review["business_id"])
    return user_ids, biz_ids

def get_users_from_id(users, user_ids):
    user_objs = []
    for i in user_ids:
        user_objs.append(filter(lambda u: u['user_id'] == i, users))
    return user_objs

def get_biz_from_id(bizs, biz_ids):
    biz_objs = []
    for i in biz_ids:
        biz_objs.append(filter(lambda u: u['business_id'] == i, bizs))
    return biz_objs

def main(funny_file, nonfunny_file):
    # FUNNY
    # with open('yelp_funny_a.json', 'r') as f:
    with open(funny_file, 'r') as f:
        json_str = f.read()
    funny_user_ids, funny_biz_ids = get_user_biz_id(json.loads(json_str))

    # with open('yelp_nonfunny_a.json', 'r') as f:
    with open(nonfunny_file, 'r') as f:
        json_str = f.read()
    nonfunny_user_ids, nonfunny_biz_ids = get_user_biz_id(json.loads(json_str))

    ### get user json
    users = []
    for line in open('yelp_academic_dataset_user.json', 'r'):
        users.append(json.loads(line))
    funny_users = get_users_from_id(users, funny_user_ids)
    nonfunny_users = get_users_from_id(users, nonfunny_user_ids)

    bizs = []
    for line in open('yelp_academic_dataset_business.json', 'r'):
        bizs.append(json.loads(line))

    funny_bizs = get_biz_from_id(bizs, funny_biz_ids)
    nonfunny_bizs = get_biz_from_id(bizs, nonfunny_biz_ids)

    print str(len(funny_users)) + ' ' + str(len(nonfunny_users)) + ' ' + str(len(funny_bizs)) + ' ' + str(len(nonfunny_bizs))

    # funny_users_output = open("funny_users_a.json", 'w')
    funny_users_output = open(funny_file.split('.')[0]+"_users.json", 'w')
    funny_users_output.write(json.dumps(funny_users))
    funny_users_output.close()

    # nonfunny_users_output = open("nonfunny_users_a.json", 'w')
    nonfunny_users_output = open(nonfunny_file.split('.')[0]+"_users.json", 'w')
    nonfunny_users_output.write(json.dumps(nonfunny_users))
    nonfunny_users_output.close()


    # funny_bizs_output = open("funny_bizs_a.json", 'w')
    funny_bizs_output = open(funny_file.split('.')[0]+"_bizs.json", 'w')
    funny_bizs_output.write(json.dumps(funny_bizs))
    funny_bizs_output.close()

    # nonfunny_bizs_output = open("nonfunny_bizs_a.json", 'w')
    nonfunny_bizs_output = open(nonfunny_file.split('.')[0]+"_bizs.json", 'w')
    nonfunny_bizs_output.write(json.dumps(nonfunny_bizs))
    nonfunny_bizs_output.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

