import json


def getUserParse(user):
    print(user)
    return json.dumps({'users':{
                       'userName': user.userName,
                       'name': user.name,
                       'lastName': user.lastName,
                       'age': user.age}})
