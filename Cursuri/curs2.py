print("Acesta e cursul al 2-lea")

name = "Ana"
if name:
    print(name)
else:
    print(name)  # this is a inline comment
    print("Nu avem definit niciun nume")

first_person = {'Name', 'John'}
second_person = {'Name', 'John'}
if first_person is second_person:
    print('they are the same')
else:
    print('they are NOT the same')

if first_person == second_person:
    print('they are the same')
else:
    print('they are NOT the same')

my_str = 'Owner\'s \r\n manual'
print(my_str)

print("""Aasfdsadsa asdsadsa\ adsds''asd  
asdsadsad
asdasd""")

msg = "{} has {} yeard.".format('Ion', 18)  # formatare
print(msg)
msg1 = "{name} has {age} yeard.".format(name='Vasile', age=19)
print(msg1)
name = 'Ion'
age = 18
msg_3 = f"{name} has {age + 2} years"
print(msg_3)
l = [1, 2, 3, 'Ana are mere', True, False, None, [4, 5, 6]]

print(l[2])

l[2] = '99'

print(l[2])

inventar = ["faina", "drojdie", "apa", "sare"]
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f'{value} cu pozitia {index}')

print(inventar[-1])
max = len(inventar)
print(max)
print(inventar[len(inventar) - 1])