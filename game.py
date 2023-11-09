l = 1
results = []    # Create an empty list to store results
data_list = []  # Create a list to store data from the file
counter = 0

# Read data from the file
while counter < 2 * l:
    with open(r"C:\Users\pohqi\Desktop\wtf.txt") as file:
        for line in file:
            data_list.append(list(map(int, line.split())))
    n, a, b = data_list[counter]
    input_array = data_list[counter + 1]
    total = 0
    temp_list = []

    # Continue until 'a' is less than 'b'
    while a < b:
        for index, value in enumerate(input_array):
            if value < a:
                temp_list.append(value)
                input_array.pop(index)
        try:
            a += max(temp_list)
            temp_list.pop(temp_list.index(max(temp_list))
            total += 1
        except ValueError:
            results.append(-1)
            break
    else:
        results.append(total)
    counter += 2

# Print the results
for res in results:
    print(res)
