def counting_sort(array):
    # max_val = max(arr)
    # count = [0] * (max_val + 1)
    # output = [-1] * len(arr)
    # for i in arr:
    #     count[i] += 1
    # for i in range(1, len(count)):
    #     count[i] += count[i - 1]
    # for i in range(len(arr) - 1, -1, -1):
    #     output[count[arr[i]] - 1] = arr[i]
    #     count[arr[i]] -= 1
    # for i in range(len(arr)):
    #     arr[i] = output[i]
    # return arr
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted Array:", counting_sort(arr))
