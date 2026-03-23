the_data = [None] * 9

the_data[0] = 20
the_data[1] = 3
the_data[2] = 4
the_data[3] = 8
the_data[4] = 12
the_data[5] = 99
the_data[6] = 4
the_data[7] = 26
the_data[8] = 4

def insertion_sort(the_data):
    for count in range(1, len(the_data)):
        data_to_insert = the_data[count]
        inserted = False
        next_value = count - 1
        while next_value >= 0 and inserted == False:
            if data_to_insert < the_data[next_value]:
                the_data[next_value + 1] = the_data[next_value]
                next_value = next_value - 1
                the_data[next_value + 1] = data_to_insert
            else:
                inserted = True

def print_array(the_data):
    for value in the_data:
        print(value)


print("Before Sorting")
print_array(the_data)

insertion_sort(the_data)

print("After Sorting")
print_array(the_data)