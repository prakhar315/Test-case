import random

def generate_test_case():
    n = random.randint(300, 750)
    nums = [random.randint(500, 700) for _ in range(n)]
    return nums

def find_shortest_subarray(nums):
    degree = {}
    max_degree = 0
    for i, num in enumerate(nums):
        if num not in degree:
            degree[num] = [i]
        else:
            degree[num].append(i)
        max_degree = max(max_degree, len(degree[num]))
    
    min_length = float('inf')
    for num, indices in degree.items():
        if len(indices) == max_degree:
            min_length = min(min_length, indices[-1] - indices[0] + 1)
    
    return min_length

def main():
    num_cases = int(input("Enter the number of test cases: "))
    sorted_array = input("Is the array sorted? (yes/no): ").lower() == 'yes'

    for _ in range(num_cases):
        nums = generate_test_case()
        if sorted_array:
            nums.sort()
        print(len(nums))
        print(" ".join(map(str, nums)))
        print()

if __name__ == "__main__":
    main()
