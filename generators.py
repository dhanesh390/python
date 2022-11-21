# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def number_sequence():
#     number = 0
#     while True:
#         yield number
#         number += 1
#
#
# for number in number_sequence():
#     if number <= 50:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')


# Using close method in generator to stop the iteration
# for number in number_sequence():
#     if number >= 50:
#         number_sequence().close()
#     else:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')

# for number in number_sequence():
#     if number >= 50:
#         number_sequence().throw(ValueError("Not more than 50"))
#     else:
#         even_number = is_even(number)
#         if even_number:
#             print(f'{number} is even')
#         else:
#             print(f'{number} is odd')

# sequence_number = (number for number in range(10))
#
# for number in sequence_number:
#     print(number)
#
#
# def even_numbers(numbers):
#     for num in range(numbers):
#         if num % 2 == 0:
#             print('even number: ', num)
#             yield num
#
#
# def square(numbers):
#     for num in numbers:
#         print('squared number: ', num ** 2)
#         yield num ** 2
#
#
# print('Sum is: ', sum(square(even_numbers(10))))

numbers = (number for number in range(0, 10, 2))
# print(sum(square(numbers)))

for number in numbers:
    print('first call: ', number)

for number in numbers:
    print('second call: ', number)


# comprehensed_list = [number**3 for number in range(1, 11) if number % 2 == 0]
# print('Comprehensed list: ', comprehensed_list)
#
# comprehensed_generator = (number**3 for number in range(0, 11) if number % 2 == 0)
# print('generator comp: ', comprehensed_generator)
# # print('sum of comp gen: ', sum(comprehensed_generator))
# for number in comprehensed_generator:
#     print(number)
#
# print('generated comp sum: ', sum(number**2 for number in range(1, 11) if number % 2 == 0))


