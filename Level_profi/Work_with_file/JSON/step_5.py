import json 

def is_correct_json(string):
    try:
        data = json.loads(string)
        
    except:
        return False
    
    return True


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))