import random

def generate_array(size, sorted_array):
    element_range = (0, 500)
    if sorted_array:
        # Generate a sorted array with multiple occurrences of zero at random indices
        array = random.choices(range(1, 501), k=size)
        num_zeros = random.randint(1, size // 2)
        zero_indices = random.sample(range(size), num_zeros)
        for idx in zero_indices:
            array[idx] = 0
        return sorted(array)
    else:
        # Generate an unsorted array with multiple occurrences of zero at random indices
        array = random.choices(range(501), k=size)
        num_zeros = random.randint(1, size)
        zero_indices = random.sample(range(size), num_zeros)
        for idx in zero_indices:
            array[idx] = 0
        return array

def main():
    sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = random.randint(1, 1000)  # Generating array size within the range of 1 to 1000
        array = generate_array(size, sorted_array)
        
        print(size)
        print(" ".join(map(str, array)))
        print()

if __name__ == "__main__":
    main()
