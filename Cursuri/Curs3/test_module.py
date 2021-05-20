# from pkg1.firs_module import *
# from pkg1.second_module import my_var as second_var, my_func as second_func
from pkg1 import *

if __name__ == '__main__':
    print(my_var)
    print(my_func())

    print(second_var)
    print(second_func())