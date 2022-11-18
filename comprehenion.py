first_list = {1: 2, 2: 3, 3: 4, 4: 5}
second_list = (2,)
third_list = [1, 2]


def add(a, b):
    return a + b


"""
 Zip function only takes iterables as input and returns a list 
 -> It can take 0 arguments as well as n number of arguments 
"""
print('Zip: ', list(zip(first_list, second_list, third_list)))
""" 
 Map takes arguments based on the function provided it works similar 
 to zip function only works until the least iterable object provided in the lists
"""
print('map : ', list(map(add, first_list, second_list)))


sample_list_one = [1, 2, 3, 4, 5, 6]
print('list 1: ', sample_list_one)
sample_list_one = [x * 2 for x in sample_list_one]
print('list 1 comp: ', sample_list_one)

sample_list_two = [[1, 2], [3, 4], [5, 6]]
print('list 2: ', sample_list_two)
sample_list_two = [y**2 for x in sample_list_two for y in x]
print('list 2 comp: ', sample_list_two)
# sample_list_two = [[y**2 for y in x] for x in sample_list_two]
# print('list 2, 2 comp: ', sample_list_two)


sample_list_three = [[['Dhanesh', 1, 2000], ['Gowtham', 0, 3000], ['Deepak', 22, 2000]], [['yuvaraj', 21, 2000], ['king', 19, 3000], ['rithi', 23]]]
sample_list_three = [(y[0], 'First batch') if y[1] >= 21 else (y[0], 'third batch') if y[1] < 20 else (y[0], 'second batch') for x in sample_list_three for y in x]
print('list 3: ', sample_list_three)

list_of_employees = [['Dhanesh', '11.07.22', 'developer'], ['Deepak', '01.07.22', 'tester'],
                     ['Gowtham', '11.07.22', 'developer']]

states = ['A', 2, 'c']
capitals = ['Chennai', 'Kochi', 'Bangalore']

primary_dictionary = {key: value for (key, value) in zip(states, capitals)}
print('primary: ', primary_dictionary)
print(primary_dictionary['A'])
print(primary_dictionary.get(3, 'NO value found'))

secondary_dictionary = {x: x ** 2 for x in first_list}
print('secondary: ', secondary_dictionary)

# employees_salary = {(employee[0], 'salary: 25000') if employee[2] == 'developer' else (employee[0], 'salary: 20000')
# if employee[2] == 'tester' else (employee[0], 'salary: 17500') for x in list_of_employees for employee in x}
# print('dict comp: ', employees_salary)


list_of_x = [1, 2, 3, 4, 5]

print([x**2 if x % 2 == 0 else x for x in list_of_x])

primary_dict = {3: 'a', True: 'b', 2.0: 'C', (3,): 'd', 'a': 'b', 2j: 'D'}
print(primary_dict)
print(hash('A'))
print(hash(False))

#  cannot compare different data types

print(1 == '1')

