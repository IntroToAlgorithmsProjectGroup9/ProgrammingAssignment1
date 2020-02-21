"""
Student Name:  Monterius Crump
        NetID: mc2730
Student Name:  Mark Hodge
        NetID: mrh598
Student Name:  David Penfield
        NetID: dep153
Student Name:  Elwood Simpson
        NetID: ets147
Student Name:  Kaleb Thornton
        NetID: krt237
Programming Language: Python 3.7 with the 'matplotlib' module
Compiler/IDE Used:    PyCharm 2019
Program Description:  Implements and compares the running times of Insertion Sort and Merge Sort
"""

import random
import time
from mergesort import mergesort
try:
    from matplotlib import pyplot
except ModuleNotFoundError:
    print(
        " Error: module 'matplotlib' not found.\n",
        "Please install with 'python3 -m pip install matplotlib' and try again."
    )
    exit(1)


# function that implements Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# function that times insertion sort with the given inputs
def time_insertion_sort(input_sizes):
    print("\nInsertion Sort: Beginning timing...")

    # init array to store results and return later
    time_arr = []

    # repeat for each input size
    for size in input_sizes:
        # setup the test array
        test_arr = random.sample(range(0, size), size)

        # print the input size
        print(f"Insertion Sort: input size: {size}", end=", ")

        # log the start time
        time_start = time.time()

        # call insertion sort
        insertion_sort(test_arr)

        # log the stop time and find the time delta
        time_stop = time.time()
        delta = time_stop - time_start

        # print results and add to time results array
        print(f"time: {delta} seconds")
        time_arr.append(delta)

    # return results
    return time_arr


# function that times merge sort with the given inputs
def time_merge_sort(input_sizes):
    print("\nMerge Sort: Beginning timing...")

    # init array to store results and return later
    time_arr = []

    # repeat for each input size
    for size in input_sizes:
        # setup the test array
        test_arr = random.sample(range(0, size), size)

        # print input size
        print(f"Merge Sort: input size: {size}", end=', ')

        # log the start time
        time_start = time.time()

        # calculate left index and right index, then call merge sort
        left_index = 0
        right_index = size - 1
        mergesort(test_arr, left_index, right_index)

        # log the stop time and find the time delta
        time_stop = time.time()
        delta = time_stop - time_start

        # print results and add to time results array
        print(f"time: {delta} seconds")
        time_arr.append(delta)

    # return results
    return time_arr


# function to plot results using matplotlib
def plot(input_size, insert_time, merge_time):
    # setup graph title and axes names
    pyplot.title("Comparison of Insertion Sort and Merge Sort Execution Times")
    pyplot.xlabel("Input Size (n)")
    pyplot.ylabel("Execution Time (in seconds)")

    # plot the graph and display it
    pyplot.plot(input_size, insert_time, label="Insertion Sort", marker='o')
    pyplot.plot(input_size, merge_time, label="Merge Sort", marker='o')
    pyplot.legend()
    pyplot.show()


def main():
    # define some input sizes to test with
    input_sizes = [500, 1000, 5000, 10000, 25000, 50000]

    # time insertion sort
    insert_times = time_insertion_sort(input_sizes)

    # time merge sort
    merge_times = time_merge_sort(input_sizes)

    # plot the results
    plot(input_sizes, insert_times, merge_times)


if __name__ == "__main__":
    main()
