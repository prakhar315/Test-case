import random

def generate_array(size, value_range):
    return [random.randint(*value_range) for _ in range(size)]

def main():
    num_cases = int(input("Enter the number of test cases: "))
    for _ in range(num_cases):
        size1 = random.randint(300, 750)
        size2 = random.randint(300, 750)
        array1 = generate_array(size1, (500, 700))
        array2 = generate_array(size2, (500, 700))
        
        print(size1, size2)
        print(" ".join(map(str, array1)))
        print(" ".join(map(str, array2)))
        print()

if __name__ == "__main__":
    main()
