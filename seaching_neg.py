import random

def generate_array(size, sorted_array, key):
    element_range = (-1000, 1000)
    # Ensure the key is in the range and the array has distinct elements
    array = random.sample(range(-1000, 1001), k=size - 1)
    array.append(key)  # Adding the key element to the array
    
    # Ensure elements are distinct by removing the key if it's already in the array
    array = list(set(array))
    
    # If duplicates removal reduces the size, add random elements to maintain size
    while len(array) < size:
        new_element = random.randint(-1000, 1000)
        if new_element not in array:
            array.append(new_element)

    if sorted_array:
        return sorted(array)
    else:
        return array

def main():
    sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'
    num_test_cases = int(input("Enter the number of test cases: "))

    for _ in range(num_test_cases):
        size = random.randint(1, 1000)  # Generating array size within the range of 1 to 1000
        key = random.randint(1, 700)  # Generating key element within the range of 1 to 700
        array = generate_array(size, sorted_array, key)
        
        print(size)
        print(" ".join(map(str, array)))
        print(f"{key}\n")

if __name__ == "__main__":
    main()
