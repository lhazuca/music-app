import json

def getUserParser(user):

    return json.dumps({'user': {'userName': user.userName,
                       'name': user.name,
                       'lastName': user.lastName}})