import json
#load the data
def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)
# making a function which users may know to like the pages
def useres_might_kown_like_pages(user_id,data):
    #making a dictionary to store the user id and its liked pages
    user_page = {}
    # populate the dictionary
    for user in data["users"]:
        user_page[user['id']] = set(user['liked_pages'])
    
    if user_id not in user_page:
        return []
#  current users liked pages directly
    direct_like_pages = user_page[user_id]
    pages_suggesections ={}
    for otheruser,pages in user_page.items():
        if otheruser != user_id:
            common_pages_beetween_two_users = direct_like_pages.intersection(pages)

        for page in pages:
            if page not in direct_like_pages:
                pages_suggesections[page] = pages_suggesections.get(page,0)+len(common_pages_beetween_two_users)

    sorted_pages_suggesitions = sorted(pages_suggesections.items(),key=lambda x:x[1],reverse=True)
    return [(page_id,score) for page_id , score in sorted_pages_suggesitions]        
data = load_data("massivdataset.json")
user_id = 1
recc = useres_might_kown_like_pages(user_id,data)
print(recc)
