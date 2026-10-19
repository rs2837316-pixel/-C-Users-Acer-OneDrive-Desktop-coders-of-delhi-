import json
def data_display(filename):
    with open(filename,"r") as f:
        data = json.load(f)
        return data

print(data_display("data.json"))


def data_users(data):
    print("users and their connections")
    for user in data["users"]:
        print(f"ID:{user['id']}-{user['name']} is a friend with:{user['friends']} and like pages are {user['liked_pages']}")

    print("\npage informations")
    for page in data["pages"]:
        print(f"{page['id']} is a {page['name']}")

data_users(data_display("data.json"))



