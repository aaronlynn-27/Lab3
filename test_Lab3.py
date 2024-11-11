import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_more_than_10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 12, 23, 53, 63]
    test = 1
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING)

    assert (result == test)

def test_bubble_no_number():
    result = []
    input_arr = []
    test = 0
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING)

    assert(result == test)

def test_bubble_no_integer():
    result = []
    input_arr = [22,14,"sg lee pl",1]
    test = 2
    result = Lab3.bubble_sort(input_arr,Lab3.SORT_DESCENDING)

    assert(result == test)