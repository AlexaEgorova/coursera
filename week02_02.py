import json
import functools

def to_json(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return json.dumps(res)
    return inner


#@to_json
#def get_data():
#    return {
#        'data': 42
#    }
#print(get_data())
