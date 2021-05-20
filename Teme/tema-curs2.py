# declare a list
l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(l)

# print ascending order
m = l.copy()
m.sort()
print('ascending sorting ')
print(m)

# print descending order
n = l.copy()
n.sort(reverse=True)
print('descending sorting ')
print(n)

# print even index elements with slice
even_index_list = l[1::2]
print('even index elements')
print(even_index_list)

# print even elements with slice
even_list = m[1::2]
even2 = [y for y in l if y % 2 == 0]
print('even elements v1 ')
print(even_list)
print('even elements v2 ')
print(even2)

# print odd index elements with slice
odd_index_list = l[::2]
print('odd index elements ')
print(odd_index_list)

# print odd elements with slice
odd_list = m[::2]
odd2 = [y for y in l if y % 2 == 1]
print('odd elements v1 ')
print(odd_list)
print('odd elements v2 ')
print(odd2)

# print multiply of 3
multiply_3 = m[2::3]
print('multiply of 3 v1 ')
print(multiply_3)

# print multiply of 3
multi = [y for y in l if y % 3 == 0]
print('multiply of 3 v2 ')
print(multi)

