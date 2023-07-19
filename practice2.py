girls = ['jane', 'ashley', 'hana']
boys = ['peter', 'jay', 'maru']
pair = zip(girls, boys)
print(pair)
print(list(pair))

for pair in zip(girls, boys):
    print(pair)

for i in range(3):
    pair = (girls[i], boys[i])
    print(pair, end=(','))


# def my_function(x, y, z):
#     print(x, y, z)

# my_dict = {'x': 1, 'y' : 2, 'z' : 3}
# my_function(**my_dict)