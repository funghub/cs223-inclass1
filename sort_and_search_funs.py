def selection_sort_iter(df, column, descending=False):

    # Keep track of row positions
    order = list(range(len(df)))

    n = len(order)

    for i in range(n - 1):

        selected_idx = i

        for j in range(i + 1, n):

            current_value = df.iloc[order[j]][column]
            selected_value = df.iloc[order[selected_idx]][column]

            if descending:
                if current_value > selected_value:
                    selected_idx = j
            else:
                if current_value < selected_value:
                    selected_idx = j

        # Swap entire row positions
        order[i], order[selected_idx] = (
            order[selected_idx],
            order[i]
        )

    # Return DataFrame in sorted row order
    return df.iloc[order].copy()

def selection_sort_recursive(
    df,
    column,
    descending=False,
    start=0,
    order=None
):

    if order is None:
        order = list(range(len(df)))

    n = len(order)

    # Base case
    if start >= n - 1:
        return df.iloc[order].copy()

    selected_idx = start

    for j in range(start + 1, n):

        current_value = df.iloc[order[j]][column]
        selected_value = df.iloc[order[selected_idx]][column]

        if descending:
            if current_value > selected_value:
                selected_idx = j
        else:
            if current_value < selected_value:
                selected_idx = j

    # Swap entire row positions
    order[start], order[selected_idx] = (
        order[selected_idx],
        order[start]
    )

    return selection_sort_recursive(
        df,
        column,
        descending,
        start + 1,
        order
    )

# Function to sort array using insertion sort iteratively
# https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
def insertionSort_i(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# https://www.geeksforgeeks.org/dsa/recursive-insertion-sort/
def insertionSort_r(arr,n):
    # base case
    if n<=1:
        return
    
    # Sort first n-1 elements
    insertionSort_r(arr,n-1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2
    
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1]=last

"""
Merge Sort, Quick Sort, and Binary Search
Each algorithm is implemented in both a recursive and an iterative form.
"""


# ---------------------------------------------------------------------------
# 1. MERGE SORT
# ---------------------------------------------------------------------------

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_recursive(arr):
    """Classic top-down recursive merge sort. O(n log n)."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)


def merge_sort_iterative(arr):
    """
    Bottom-up iterative merge sort.
    Repeatedly merges sorted runs of doubling size (1, 2, 4, 8, ...)
    instead of recursing.
    """
    arr = arr[:]
    n = len(arr)
    width = 1

    while width < n:
        for start in range(0, n, 2 * width):
            mid = min(start + width, n)
            end = min(start + 2 * width, n)
            merged = merge(arr[start:mid], arr[mid:end])
            arr[start:end] = merged
        width *= 2

    return arr


# ---------------------------------------------------------------------------
# 2. QUICK SORT
# ---------------------------------------------------------------------------

def _partition(arr, low, high):
    """Lomuto partition scheme; pivot = last element. Sorts in place."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_recursive(arr, low=0, high=None):
    """Classic recursive quick sort. Sorts in place. Average O(n log n)."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort_recursive(arr, low, pivot_index - 1)
        quick_sort_recursive(arr, pivot_index + 1, high)

    return arr


def quick_sort_iterative(arr):
    """
    Iterative quick sort using an explicit stack to simulate
    the recursion. Sorts in place.
    """
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = _partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr


# ---------------------------------------------------------------------------
# 3. BINARY SEARCH
# ---------------------------------------------------------------------------

def binary_search_recursive(arr, target, low=0, high=None):
    """
    Recursive binary search on a sorted list.
    Returns the index of target, or -1 if not found.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


def binary_search_iterative(arr, target):
    """
    Iterative binary search on a sorted list.
    Returns the index of target, or -1 if not found.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

