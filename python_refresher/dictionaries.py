# Dictionaries: Store data by key/value
my_set = {1, 3, 5}                      # Set
my_dict = {'name': 'Jose', 'age': 90}
another_dict = { 1: 15, 2: 75, 3: 150}

# Tuple within Dictionary
lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 45, 65, 23, 22)
}

# Dictionary within Dictionary
universities = {
    #dict1: {'name': 'MIT', 'location': 'US'},
    #dict2: dict(name='MIT', location='US')

}

print sum(lottery_player['numbers'])

lottery_player['name'] = 'John'
# lottery_player['numbers'][0] = 50 # TypeError: 'tuple' object does not support item assignment

