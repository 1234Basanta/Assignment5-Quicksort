import random
import time


# Deterministic Quicksort
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)


# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# Function to compare algorithms
def compare_algorithms(data, title):

    print("\n==============================")
    print(title)
    print("==============================")

    start = time.perf_counter()
    deterministic_quicksort(data.copy())
    end = time.perf_counter()

    print("Deterministic:", round(end - start, 6), "seconds")

    start = time.perf_counter()
    randomized_quicksort(data.copy())
    end = time.perf_counter()

    print("Randomized   :", round(end - start, 6), "seconds")


# Random data
random_data = [random.randint(1, 10000) for _ in range(1000)]

# Sorted data
sorted_data = sorted(random_data)

# Reverse sorted
reverse_data = sorted(random_data, reverse=True)

compare_algorithms(random_data, "Random Data")
compare_algorithms(sorted_data, "Sorted Data")
compare_algorithms(reverse_data, "Reverse Sorted Data")