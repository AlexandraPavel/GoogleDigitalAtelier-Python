import random
import copy

elements = [x for x in range(11)]

# print(choices)
while True:
    random_choice = random.choice(elements)
    if random_choice % 3 == 0:
        break
    print(f'Random choice is {random_choice}')

print(f'Exit random choice is {random_choice}')

for i in range(11):
    if i % 2 != 0:
        continue
    print(f'Numar par: {i}')

my_sum = 0
# URL = 'http://my-company.com'
# URL = 'http://local.my-company.com:8080'


def get_sum(a, b):
    # global my_sum
    my_sum = a + b
    print(my_sum)

get_sum(1, 2)
print(my_sum)

l1 = [1, 2, 3, [2, 3, 4]]

l2 = copy.deepcopy(l1) # prin valoare
# l2 = list(l1) # prin referinta
l2[3].append(4)

print(l1)
print(l2)


def my_function(nume, prenume, *args, **kwargs):
    tail = ' '.join(args)
    print(f'{nume} {prenume} {tail}')

    for key in kwargs.keys():
        print(f'key: {key} has value: {kwargs[key]}')


my_function('popescu', 'ana', 'are', '2', 'mere', job='developer', age=22)


while True:
    my_var = input('Introduceti un nr: ')
    try:
        my_int = int(my_var)
        # print(my_var)
        # print(my_ints)
        # s = my_int + c
    except ValueError as e:
        print('Please enter a numeric value')
    except NameError:
        print('You have used an undefined var')
        pass
    else:
        print('No exception occurred')
    finally:
        print('We will print this if there\'s an exception or not')

print(dir(__builtins__))


def my_function1():
    # enclosing function
    def my_second_function():
        # msg = 'lolo'
        print(f'my_second_function {msg}')
    msg = 'Hello World'
    my_second_function()
    print(f'my_function {msg}')


my_function1()


