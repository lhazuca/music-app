import json

def getUserLoginParser(userLogin):

    return json.dumps({'userLogin': {'userName': userLogin.userName,
                                    'password': userLogin.password}})