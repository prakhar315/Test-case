import random

def generate_majority_array(size):
    element_range = (-1000, 1000)
    majority_count = size // 2 + 1
    majority_element = random.randint(-1000, 1000)

    # Create the array with the majority element appearing `majority_count` times
    array = [majority_element] * majority_count
    
    # Fill the rest of the array with random elements
    while len(array) < size:
        element = random.randint(-1000, 1000)
        if element != majority_element:
            array.append(element)
    
    # Shuffle to avoid any ordering
    random.shuffle(array)
    return array, majority_element

def main():
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = random.randint(3, 1000)  # Generating array size within the range of 3 to 1000
        array, majority_element = generate_majority_array(size)
        
        print(size)
        print(" ".join(map(str, array)))
        print(f"{majority_element}\n")

if __name__ == "__main__":
    main()
