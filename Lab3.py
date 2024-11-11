print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # Return 0 if no numbers are entered (REQ 4)
    if n == 0:
        return 0  
    
    # Return 1 if 10 or more numbers are entered (REQ 3)
    elif n >= 10:
        return 1  

    # Return 2 if any element is not an integer (REQ 5)
    for x in arr:
        if not isinstance(x, int):
            return 2   

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = -1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr_2 = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
    arr_3 = []
    arr_4 = ['ET0735', 1, 2, 3, 4, 5, 'DevOPs']

     # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    # If >= 10 numbers are entered
    print("If >= 10 numbers are entered ")
    result = bubble_sort(arr_2, SORT_ASCENDING)
    print(result)

    # If 0 numbers are entered
    print("If 0 numbers are entered")
    result = bubble_sort(arr_3, SORT_ASCENDING)
    print(result)

    # If any of the values entered are not integers 
    print("If any of the value entered are not integers ")
    result = bubble_sort(arr_4, SORT_ASCENDING)
    print(result)

if __name__ == "__main__":
    main()


