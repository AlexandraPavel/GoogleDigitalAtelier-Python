from pkg import *
import numbers


# calculate the sum of the integers or float parameters
def sum_numbers(*args, **kwargs):
    # tail = ' '.join(args)
    if not args:
        return 0
    sum = 0
    for y in args:
        if isinstance(y, numbers.Number):
            sum += y
    return sum


sum1 = sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad'])
sum2 = sum_numbers()
sum3 = sum_numbers(2, 4, 'abc', param_1=2)

print(f'sum1 = {sum1} \nsum2 = {sum2} \nsum3 = {sum3}')


# function that reads input I/O and return the value of
# a integer or 0 if is not an integer
def verify_integer():
    my_var = input('Introduceti un nr: ')
    try:
        my_int = int(my_var)
    except ValueError as e:
        return 0
    except NameError:
        print('You have used an undefined var')
        pass
    else:
        return my_int
    # finally:
    #     print('We will print this if there\'s an exception or not')
    #     # return my_int


print(verify_integer())
print(sum_of_all(5))
print(sum_even(5))
print(sum_odd(5))
