import connexion

def app01(body):
    uid = connexion.request.headers.get("X_uid")
    print(f"uid:{uid}")

    return {"method": "app/app01", "uid": uid}, 200