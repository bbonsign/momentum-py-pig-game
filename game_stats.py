import json


def update_stats(name):
    with open('stats', 'r') as f:
        loaded_stats = json.load(f)
        if loaded_stats == '':
            loaded_stats = {'Bot': 0, 'Human': 0}
    loaded_stats[name] += 1
    encoded_stats = json.JSONEncoder().encode(loaded_stats)
    with open('stats', 'w') as f:
        f.write(encoded_stats)


def print_stats():
    with open('stats', 'r') as f:
        loaded_stats = json.load(f)
        if loaded_stats == '':
            loaded_stats = {'Bot': 0, 'Human': 0}
    for key in loaded_stats:
        print(f"====> Total {key} wins: {loaded_stats[key]} <====")
    print('\n\n')


def clear_stats():
    with open('stats', 'w') as f:
        f.write("{'Bot': 0, 'Human': 0}")


