import itertools

# flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
# flower_names = input()

for i in range(3):
    my_iter = itertools.combinations(flower_names, i + 1)
    for element in my_iter:
        print(element)



