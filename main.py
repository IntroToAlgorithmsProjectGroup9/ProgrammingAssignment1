import random, time

# function that implements Insertion Sort
def insertion_sort(arr):

    # Get time at start of sort.
    timeStart = time.time()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    # Get time at end of sort and calculate total elapsed time.
    timeStop = time.time()
    elapsedTime = (timeStop - timeStart)
    print("Time Elapsed: " + str(elapsedTime) + " Start Time: "  + str(timeStart) + " Stop Time: " + str(timeStop))

    return (elapsedTime)


def main():
    print("Hello World!")
    insertionSizes = [500, 1000, 5000, 10000, 25000, 50000]
    insertionTimes = []

    # Insertion-Sort a 500 element array
    res = random.sample(range(0, 50000), 500)
    time = insertion_sort(res)
    insertionTimes.append(time)

    # Insertion-Sort a 1,000 element array
    res = random.sample(range(0, 50000), 1000)
    time = insertion_sort(res)
    insertionTimes.append(time)

    # Insertion-Sort a 5,000 element array
    res = random.sample(range(0, 50000), 5000)
    time = insertion_sort(res)
    insertionTimes.append(time)

    # Insertion-Sort a 10,000 element array
    res = random.sample(range(0, 50000), 10000)
    time = insertion_sort(res)
    insertionTimes.append(time)

    print(insertionTimes)

    # Insertion-Sort a 25,000 element array
    res = random.sample(range(0, 50000), 25000)
    time = insertion_sort(res)
    insertionTimes.append(time)

    # Insertion-Sort a 50,000 element array
    res = random.sample(range(0, 50000), 50000)
    time = insertion_sort(res)
    insertionTimes.append(time)

main()



