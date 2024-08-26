import json, os

def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        return {}
    

def read_user_by_id(username, password):
    data = load_json('data/users.json')
    if username in data and data[username]['password'] == password:
        return True
    else:
        return False
