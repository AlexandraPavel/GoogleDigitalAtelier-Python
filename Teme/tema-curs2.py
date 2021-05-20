# declare a list
l = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(l)

# print ascending order
m = l.copy()
m.sort()
print(m)
print(l)

# print descending order
n = l.copy()
n.sort(reverse=True)
print(n)

# print even elements with slice
even_list = m[1::2]
print(even_list)

# print odd elements with slice
odd_list = m[::2]
print(odd_list)

# print multiply of 3
multiply_3 = m[2::3]
print(multiply_3)

