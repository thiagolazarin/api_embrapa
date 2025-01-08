from app import auth

USERS = {
    "thiago": "senha"
}

@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None