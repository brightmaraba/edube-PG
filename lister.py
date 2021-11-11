import cProfile
import time


with cProfile.Profile() as cp:
    start_time = time.time()
    my_list = [8, 10, 6, 2, 4]
    swapped = True

    while swapped:
        swapped = False  # Initial state - No swaps yet
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True  # Swap occurred
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print(my_list)
    stop_time = time.time()
    print(f"Time elapsed: {stop_time - start_time}")

cp.print_stats()
