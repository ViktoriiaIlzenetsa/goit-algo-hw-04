import timeit
import random

from merge_sort import merge_sort
from insertion_sort import insertion_sort

if __name__ == "__main__":
    small_data = [random.randint(0, 1000) for _ in range(1000)]
    medium_data = [random.randint(0, 10000) for _ in range(10000)]
    large_data = [random.randint(0, 100000) for _ in range(100000)]

    time_small_merge = timeit.timeit(lambda: merge_sort(small_data[:]), number = 10)
    time_small_insertion = timeit.timeit(lambda: insertion_sort(small_data[:]), number = 10)
    time_small_tim_sorted = timeit.timeit(lambda: sorted(small_data[:]), number = 10)
    time_small_tim_sort = timeit.timeit(lambda: small_data[:].sort(), number = 10)

    time_medium_merge = timeit.timeit(lambda: merge_sort(medium_data[:]), number = 10)
    time_medium_insertion = timeit.timeit(lambda: insertion_sort(medium_data[:]), number = 10)
    time_medium_tim_sorted = timeit.timeit(lambda: sorted(medium_data[:]), number = 10)
    time_medium_tim_sort = timeit.timeit(lambda: medium_data[:].sort(), number = 10)

    time_large_merge = timeit.timeit(lambda: merge_sort(large_data[:]), number = 5)
    time_large_insertion = timeit.timeit(lambda: insertion_sort(large_data[:]), number = 1)
    time_large_tim_sorted = timeit.timeit(lambda: sorted(large_data[:]), number = 5)
    time_large_tim_sort = timeit.timeit(lambda: large_data[:].sort(), number = 5)

    print(f"|{'Algorithm':<20} | {'Time for small data':<25} | {'Time for medium data':<25} | {'Time for large data':<25} |")
    print(f"|{'-'*21}|{'-'*27}|{'-'*27}|{'-'*27}|")
    print(f"|{'Merge sort':<20} | {time_small_merge:<25} | {time_medium_merge:<25} | {time_large_merge:<25} |")
    print(f"|{'Insertion sort':<20} | {time_small_insertion:<25} | {time_medium_insertion:<25} | {time_large_insertion:<25} |")
    print(f"|{'Tim sort sorted':<20} | {time_small_tim_sorted:<25} | {time_medium_tim_sorted:<25} | {time_large_tim_sorted:<25} |")
    print(f"|{'Tim sort sort':<20} | {time_small_tim_sort:<25} | {time_medium_tim_sort:<25} | {time_large_tim_sort:<25} |")
