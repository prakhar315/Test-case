import random

def generate_array_with_pivot(size, sorted_array):
    if sorted_array:
        # Generate a sorted array with a pivot element
        pivot_index = random.randint(1, size - 2)  # Ensure pivot is not at the edges
        left_sum = sum(random.choices(range(-1000, 1001), k=pivot_index))
        right_sum = sum(random.choices(range(-1000, 1001), k=size - pivot_index - 1))
        pivot_value = max(left_sum, right_sum) + 1  # Ensure pivot is greater than max sum
        array = [random.randint(-1000, 1000) for _ in range(pivot_index)]
        array.append("pivot")
        array += [random.randint(-1000, 1000) for _ in range(size - pivot_index - 1)]
        return array
    else:
        # Generate an unsorted array with a pivot element
        pivot_index = random.randint(1, size - 2)  # Ensure pivot is not at the edges
        left_sum = sum(random.choices(range(-1000, 1001), k=pivot_index))
        right_sum = sum(random.choices(range(-1000, 1001), k=size - pivot_index - 1))
        pivot_value = max(left_sum, right_sum) + 1  # Ensure pivot is greater than max sum
        array = []
        for i in range(size):
            if i < pivot_index:
                array.append(random.randint(-1000, 1000))
            elif i == pivot_index:
                array.append("pivot")
            else:
                array.append(random.randint(-1000, 1000))
        return array

def main():
    sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = random.randint(1, 500)  # Generating array size within the range of 1 to 500
        array = generate_array_with_pivot(size, sorted_array)
        
        print(size)
        print(" ".join(map(str, array)))
        print()

if __name__ == "__main__":
    main()
