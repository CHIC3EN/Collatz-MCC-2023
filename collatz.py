def dragon_procedure(n, k, numbers):
    for _ in range(k):
        for i in range(n):
            if numbers[i] % 2 == 0:
                numbers[i] //= 2
            else:
                numbers[i] = 3 * numbers[i] + 1
    return sum(numbers)

# Example usage:
n, k = 6, 1
numbers = [1, 16, 16, 14, 16, 16]
result = dragon_procedure(n, k, numbers)
print(result)  # This will print 33 for the sample input.
