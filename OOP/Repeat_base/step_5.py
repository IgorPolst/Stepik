import json
from functools import wraps

def jsonify(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):        
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}
    
print(make_user(4, False, None))