def get(token):
    print("------in auth get mehtod-----")
    # print(key)
    if token == "pass":
        return True, 200
    else:
        return False, 400

def post(body):
    print("------in auth post mehtod-----")
    print(body)
    judge = body.get('headers').get('token_yj')
    print(judge)
