import json


def check_empty():
    with open('stats', 'r') as f:
        txt = f.read()
        if txt == '':
            loaded_stats = {'Bot': 0, 'Human': 0}
        else:
            return
    encoded_stats = json.JSONEncoder().encode(loaded_stats)
    with open('stats', 'w') as f:
        f.write(encoded_stats)


def update_stats(name):
    check_empty()
    with open('stats', 'r') as f:
        loaded_stats = json.load(f)
    loaded_stats[name] += 1
    encoded_stats = json.JSONEncoder().encode(loaded_stats)
    with open('stats', 'w') as f:
        f.write(encoded_stats)


def center(value):
    return str(value).center(15)

def make_stars(n):
    return '*'*n


def print_stats():
    check_empty()
    with open('stats', 'r') as f:
        loaded_stats = json.load(f)
    print()
    for key in loaded_stats:
        key_text = f"==> Total {key} wins:".rjust(23)
        print(f"{key_text} {loaded_stats[key]} | {make_stars(loaded_stats[key])}")
    print('\n')


def clear_stats():
    with open('stats', 'w') as f:
        f.write('{"Bot": 0, "Human": 0}')
