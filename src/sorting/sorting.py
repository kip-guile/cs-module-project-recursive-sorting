# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    curA = 0
    curB = 0
    mergestate = 0
    # pointerA = arrA[curA]
    # pointerB = arrB[curB]
    while curA < len(arrA) and curB < len(arrB):
        if arrA[curA] < arrB[curB]:
            merged_arr[mergestate] = arrA[curA]
            curA += 1
            mergestate += 1
        else:
            merged_arr[mergestate] = arrB[curB]
            curB += 1
            mergestate += 1

    while curA < len(arrA):
        merged_arr[mergestate] = arrA[curA]
        curA += 1
        mergestate += 1

    while curB < len(arrB):
        merged_arr[mergestate] = arrB[curB]
        curB += 1
        mergestate += 1

    return merged_arr


arrA = [1, 3, 5, 7]
arrB = [2, 4, 6, 8]
print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    pass

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
