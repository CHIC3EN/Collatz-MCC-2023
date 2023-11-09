numbers = []
def separate_continuous_sequences(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    print("Sorted cards: ", numbers)

    sequences = []  # List to store the sequences
    current_sequence = []  # List for the current sequence
    sequence_number = 1  # Starting sequence number

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1] + 1:
            current_sequence.append(numbers[i - 1])
        else:
            current_sequence.append(numbers[i - 1])
            sequences.append(current_sequence)
            current_sequence = []
            sequence_number += 1

    # Append the last sequence
    if current_sequence:
        current_sequence.append(numbers[-1])
        sequences.append(current_sequence)

    # Create dictionary with sequence names
    sequence_dict = {f'list({i})': sequence for i, sequence in enumerate(sequences, 1)}

    return sequence_dict

def calculate_differences(sequences):
    differences = {}  # Dictionary to store the differences

    for i in range(1, len(sequences)):
        current_sequence = sequences[f'list({i})']
        next_sequence = sequences[f'list({i + 1})']
        
        last_value_current = current_sequence[-1]
        first_value_next = next_sequence[0]
        
        difference_key = f'{i}|{i+1}'
        difference_value = first_value_next - last_value_current
        
        differences[difference_key] = difference_value

    return differences

def find_highest_combo(differences, wild_card):
    highest_combo = 0
    sequences = list(separate_continuous_sequences(numbers).values())  # Extract the sequences from the dictionary
    difference_keys = list(differences.keys())

    def calculate_combo(sequence_1, sequence_2, wild_card):
        return len(sequence_1) + len(sequence_2) + wild_card

    for i in range(len(difference_keys)):
        current_combo = 0
        remaining_wild_card = wild_card
        sequence_1_key, sequence_2_key = difference_keys[i].split('|')
        sequence_1 = sequences[int(sequence_1_key) - 1]
        sequence_2 = sequences[int(sequence_2_key) - 1]
        
        for j in range(i, len(difference_keys)):
            current_difference = differences[difference_keys[j]]
            while current_difference > 0 and remaining_wild_card > 0:
                current_difference -= 1
                remaining_wild_card -= 1
            current_combo = calculate_combo(sequence_1, sequence_2, wild_card - remaining_wild_card)
            if current_combo > highest_combo:
                highest_combo = current_combo

    return highest_combo

# Example usage:
numbers = [50, 246, 36, 91, 223, 263, 176, 224, 241, 162, 292, 230, 111, 50, 242, 158, 232, 237, 113, 272, 174, 187, 191, 203, 251, 138, 103, 130, 236, 139, 79, 155, 152, 163, 215, 110, 293, 183, 293, 300, 240, 246, 223, 231, 58, 39, 300, 52, 209, 277, 98, 73, 248, 215, 282, 15, 271, 121, 276, 205, 9, 44, 25, 118, 115, 215, 101, 156, 75, 245, 293, 207, 84, 39, 142, 272, 102, 271, 261, 19]
wild_card = 20

sequences = separate_continuous_sequences(numbers)
differences = calculate_differences(sequences)
highest_combo = find_highest_combo(differences, wild_card)
for key, value in sequences.items():
    print(f'{key}: {value}')
for key, value in differences.items():
    print(f'{key}: {value}')
print(f'Highest Combo: {highest_combo}')
