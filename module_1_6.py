#Словари
my_dict = {'Alex': 1997, 'Masha': 1993, 'Sveta': 1976, 'Dima': 1972}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('Tanya'))
my_dict['Tanya'] = 1992
my_dict['Vika'] = 1998
print('Deleted value:', my_dict['Dima'])
print('Added values:', my_dict['Tanya'], 'and', my_dict['Vika'])
del my_dict['Dima']
print('Modified dictionary:', my_dict)

#Множества
my_set = {1, 2.145, 1, 2, 3,'Alex', 4, 3, 2, 2.145, 1, 4, 5, 2.145, 'Alex'}
print('Set:', my_set)
my_set.add(6)
my_set.add('Masha')
my_set.discard(1)
print('Modified set:', my_set)