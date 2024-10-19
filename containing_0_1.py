import random

def generate_array(size, sorted_array):
    element_range = (0, 1)
    if sorted_array:
        return sorted(random.choices(range(2), k=size))
    else:
        return random.choices(range(2), k=size)

def main():
    sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = random.randint(1, 50)  # Generating array size within the range of 1 to 1000
        array = generate_array(size, sorted_array)
        
        print(size)
        print(" ".join(map(str, array)))
        print()

if __name__ == "__main__":
    main()
