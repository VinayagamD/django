s = "django"
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])
print(s[::-1])

l = [3, 7, [1, 4, 'Hello']]
l[2][2] = "goodbye"
print(l)

d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

myset = set(mylist)

print(myset)

age = 4
name = "sammy"

print("Hello my dog's name is {name} and he is {age} years old".format(name=name, age=age))
print(f"Hello my dog's name is {name} and he is {age} years old")
