import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_array(size, element_range, is_sorted):
    arr = [random.randint(element_range[0], element_range[1]) for _ in range(size)]
    if is_sorted:
        arr.sort()
    return arr

def main():
    num_test_cases = int(input("Enter the number of test cases: "))
    is_sorted = input("Is the array sorted? (yes/no): ").lower() == 'yes'

    for _ in range(num_test_cases):
        print()
        size = random.randint(1, 650)  # Updated size range
        array_element_range = (1, 600)  # Updated element range
        target_range = (1, 1000)  # Updated target range

        # Generating array
        arr = generate_array(size, array_element_range, is_sorted)
        print(size)
        print(" ".join(map(str, arr)))

        # Generating target
        target_present = random.choice([True, False])  # Randomly decide if the target is present or not
        if target_present:
            target = random.choice(arr)
        else:
            target = random.randint(target_range[0], target_range[1])
        print(target)

if __name__ == "__main__":
    main()
