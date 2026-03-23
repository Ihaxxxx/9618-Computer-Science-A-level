animals = [None] * 10

animals[0] = "horse"
animals[1] = "lion"
animals[2] = "rabbit"
animals[3] = "mouse"
animals[4] = "bird"
animals[5] = "deer"
animals[6] = "whale"
animals[7] = "elephant"
animals[8] = "kangaroo"
animals[9] = "tiger"


def sort_descending():
    array_length = len(animals)

    for x in range(array_length - 1):
        for y in range(array_length - 2):
            if animals[y][0] < animals[y + 1][0]:
                temp = animals[y]
                animals[y] = animals[y + 1]
                animals[y + 1] = temp


sort_descending()

for animal in animals:
    print(animal)