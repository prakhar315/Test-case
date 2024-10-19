import random

def generate_array(size, start, end, sorted_array):
    array = list(range(start, end + 1))  # Create an array with all elements from start to end
    if sorted_array:
        random.shuffle(array)  # Shuffle if array is supposed to be unsorted
    return array

def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = end - start + 1  # Size of array is the range
        sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'
        array = generate_array(size, start, end, sorted_array)

        print(size)
        print(" ".join(map(str, array)))
        print()

if __name__ == "__main__":
    main()
