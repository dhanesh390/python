# import random  # Multiple imports should be on separate lines
# import myconstants
#
#
# class BlackJack:
#
#     def __init__(self):  # Method belongs to the class
#         pass
#
#     """ Surround method definitions within the class with one blank line"""
#
#     def first_method(self):
#         return None
#
#
# # Surround function and class with Two blank spaces between them
# def deal_card():
#     """ Returns a random card from the deck"""
#     cards = [
#         11, 1, 2, 3, 4,
#         5, 6, 7, 8, 9,
#         10, 10, 10, 10
#     ]
#     card = random.choice(cards)  # Picks up a random card from the deck
#     return card
#
#
# print(deal_card())
#
#
# def calculate_average(
#         first_number, second_number,  # Should provide four extra white spaces for arguments to differentiate from
#         third_number, fourth_number):
#     first_average = (first_number
#                      + second_number) / 2  # Break the line before the binary operator
#
#     second_average = (third_number
#                       + fourth_number) / 2  # Surround binary operators with equal spaces on both sides
#
#     return (first_average + second_average) / 2
#
#
# average = calculate_average(3, 5, 6, 7)  # Should provide a white space after ','
# print(average)
#
# next_calculation = input('Do you want to proceed to next operation: "Yes" or "No" :').capitalize()
# print(next_calculation)
#
# if next_calculation == myconstants.YES:
#     total = deal_card() * average
#     print(total)
#
# else:
#     print("Completed the calculation")

# x = 1
# y = 1
#
# print(id(x))
# print(id(y))
# z = [1, 2, 3, 4]
# print('initial list: ', id(z))
# z.append(5)
# print('appended list: ', id(z))


def generate():
    # print('id of i: ', id(i))
    i = 0
    yield i**2


for y in range(3):
    print('id of y: ', id(y))
    print(id(generate()))
    z = generate()
    next(z)
    print('z is :', z)
    print('genrated: ', list(z))
    print('id of generated y: ', id(z))

