def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(my_list)
#compare second elements to first element, if its smaller swap them
#do the same with the second and third, if you swap them compare it to the first one that was swapped with the third
#compare each element with elements that come before it, move larger elements to the right until they are in the correct spot
#repeat this until it is sorted