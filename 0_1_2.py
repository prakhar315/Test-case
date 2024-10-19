#this code will generate array having 0,1 and 2

import random

def generate_array(size, sorted_array):
    if sorted_array:
        # Generate a sorted array with multiple occurrences of zero, one, and two at random indices
        array = [0] * size
        num_ones = random.randint(1, size)
        one_indices = random.sample(range(size), num_ones)
        for idx in one_indices:
            array[idx] = 1
        
        num_twos = random.randint(1, size)
        two_indices = random.sample(range(size), num_twos)
        for idx in two_indices:
            array[idx] = 2

        return array
    else:
        # Generate an unsorted array with multiple occurrences of zero, one, and two at random indices
        array = []
        num_zeros = random.randint(1, size)
        zero_indices = random.sample(range(size), num_zeros)
        for i in range(size):
            if i in zero_indices:
                array.append(0)
            else:
                array.append(random.randint(1, 2))
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
