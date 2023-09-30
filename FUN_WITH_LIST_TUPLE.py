# Get user input
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Create a list to store the sorted tuples
sorted_tuples = []

for tuple in tuple_list:

    for i in range(len(sorted_tuples)):
        if tuple[-1] < sorted_tuples[i][-1]:
            sorted_tuples.insert(i, tuple)
            break
    else:
        sorted_tuples.append(tuple)

print("Sorted Tuples:", sorted_tuples)# Print the sorted tuples