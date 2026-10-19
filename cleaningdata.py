import json

def cleaned_data(data):
    #remove user with missing name
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    # remove the duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # remove the empty list
    data["users"] = [user for user in data["users"] if user['friends'] or user['liked_pages']]

    # to remove a duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page['id']] = page

    data['pages'] = list(unique_pages.values())    
    return data

#load the data
data = json.load(open("data2.json"))
data = cleaned_data(data)

# to dump the data
json.dump(data,open("cleaned_data2.json","w"),indent=4)
print("data has been cleaned sucessfully")





