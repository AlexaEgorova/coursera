import argparse
import os
import tempfile
import json

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', nargs = '?', required = True)
    parser.add_argument('--val', nargs = '+')
    return parser


def add_value(key, val, store):
    if key in store:
        for i in val:
            if i in store[key]:
                pass
            else:
                store[key].append(i)
    else:
        store[key] = val
    with open(storage_path, 'w') as s:
        s.write(json.dumps(store)) 


def print_values(key, store):
    if key not in store:
        print(None)
    else: 
        print(*store[key], sep=', ')

parser = createParser()
namespace = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
    store = {}
else:
    with open(storage_path, 'r') as s:
        store = json.loads(s.read())

if namespace.val is None:
    print_values(namespace.key, store)

else:
    add_value(namespace.key, namespace.val, store)


