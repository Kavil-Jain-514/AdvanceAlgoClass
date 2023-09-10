def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    #count and output arrays
    count = [0] * range_val
    output = [0] * len(arr)

    #count occurances of the elements
    for num in arr:
        count[num - min_val] +=1

    #output array
    idx = 0
    for i in range(range_val):
        while count[i] > 0:
            output[idx] = 1 + min_val
            idx += 1
            count[i] -= 1
    return output     

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    n = len(arr)
    output = [0] * n
    while max_val // exp > 0:
        count = [0] * 10

        #store count of occurances
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

    #Build the output array
    i = n-1
    while i>=0:
        index  = (arr[i]//exp)
        output[count[index%10]-1] = arr[i]
        count[index%10] -= 1
        i -= 1

    #take output array to arr[], for sorted number
    for i in range(0, len(arr)):
        arr[i] = output[i]
        exp *= 10
    return arr


#define hybrid sort

def hybrid_sort(arr):
    max_val = max(arr)
    range_val = max_val - min(arr) + 1

    #compare range length
    if range_val < len(arr):
        print("Counting sort was selected")
        return counting_sort(arr)
    else:
        print("Radix sort was selected")
        return radix_sort(arr)

#Collect user input

if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers with spaces seperated").split()))  
    sorted_arr = hybrid_sort(arr)
    print("Sorted Array: ", sorted_arr)   