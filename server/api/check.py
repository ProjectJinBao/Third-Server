import connexion

def check(body):
    print(body)
    status_code = int(connexion.request.headers.get('code'))
    # status_code = body.get('code')
    return True, status_code

def get():
    token = connexion.request.headers.get("X_some_key")
    print(connexion.request.headers)
    print(token)

    x_token = connexion.request.headers.get("X_token")
    print(x_token)

    if x_token == "error":
        return {}, 400
    if token == "yujing":
        return {"method": "get", "user_id": "2"}, 200
    elif token == "error":
        return {}, 400
    else:
        return {"method": "get", "user_id": "3"}, 532