my_set = {1, 3, 5, 5}
my_dict = {'name': 'Jose', 'age': 90, 'grades': [13, 45, 66, 90]}
another_dict = {1: 15, 2: 75, 3: 150}

lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 66, 45, 23, 22)
}

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

sum(lottery_player['numbers'])

universities[1]['location'] = 'EUA'

print(len(lottery_player['numbers']))