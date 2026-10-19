import json

def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)

def people_you_may_know(user_id,data):
    user_friend = {}

    for user in data['users']:
        user_friend[user['id']] = set(user['friends'])

    if user_id not in user_friend:
        return []

    direct_friends = user_friend[user_id]
    suggesation = {}
    # print(user_dict)
    for friend in direct_friends:
        for mutual in user_friend[friend]:
            if mutual !=user_id and mutual not in direct_friends: 
                # count the mutal friends
                suggesation[mutual] = suggesation.get(mutual,0)+1
    #now update the suggesations
    sorted_suggetions = sorted(suggesation.items(),key=lambda x:x[1] ,reverse=True)
    return [userid for userid,mutal_score in sorted_suggetions]
data = load_data("massivdataset.json")
user_id = 23
recc = people_you_may_know(user_id,data)
print(recc)

