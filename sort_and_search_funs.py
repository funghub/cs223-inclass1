# coding: utf-8 # <- This is an encoding declaration

import sys

# ---------------------------------------------------------------------------
# 1. INSERTION SORT
# ---------------------------------------------------------------------------

# Function to sort array using insertion sort iteratively
# https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/
def insertionSort_iter(df,
    column,
    descending=False,
    ):
    """Sorts a DataFrame by a specified column using an iterative Insertion Sort algorithm with index tracking."""
    order = list(range(len(df)))

    for i in range(1, len(order)):
        key_pos = order[i]
        key_val = df.iloc[key_pos][column]
        j = i - 1

        # Loop backwards through sorted portion (0 to i-1)
        while j >= 0:
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            current_val = df.iloc[order[j]][column]
                
            # Determine if current_val is out of order relative to key_val:
            # - If descending=True: shift if current_val < key_val (push smaller values right)
            # - If descending=False: shift if current_val > key_val (push larger values right)
            should_shift = (current_val < key_val) if descending else (current_val > key_val)

            if should_shift:
                order[j + 1] = order[j]
                j -= 1
            else:
                break

        order[j + 1] = key_pos

        # Reconstruct DataFrame with original index preserved order
    return df.iloc[order].copy()
    
# https://www.geeksforgeeks.org/dsa/recursive-insertion-sort/
def insertionSort_recursive(df, 
                            column, 
                            descending=False, 
                            n=None, 
                            order=None):
    """Sorts a DataFrame by a specified column using a recursive Insertion Sort algorithm with index tracking."""
    
    # base setup
    if order is None:
        order = list(range(len(df)))
    if n is None:
        n = len(order)

    # base case
    if n <= 1:
        return df.iloc[order].copy() if n == len(df) else order
    
    # Sort first n-1 elements
    insertionSort_recursive(df, column, descending=descending, n=n - 1, order=order)
    '''Insert last element at its correct position
        in sorted array.'''

    # Store the last row index pointer and its column value
    last_pos = order[n - 1]
    last_val = df.iloc[last_pos][column]
    j = n - 2
    
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while j >= 0:
        current_val = df.iloc[order[j]][column]

        # Shift check matching your iterative logic
        should_shift = (current_val < last_val) if descending else (current_val > last_val)

        if should_shift:
            order[j + 1] = order[j]
            j -= 1
        else:
            break

    # Insert last_pos into its correct sorted position
    order[j + 1] = last_pos

    # Return reconstructed DataFrame only on the outermost call completion
    return df.iloc[order].copy()

# ---------------------------------------------------------------------------
# 2. SELECTION SORT
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# 3. MERGE SORT
# ---------------------------------------------------------------------------

def merge_sort(df, column, left, right, descending):
    '''merge two lists and returns sorted elements '''

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        left_value = df.iloc[left[i]][column]
        right_value = df.iloc[right[j]][column]

        if descending:
            take_left = left_value >= right_value
        else:
            take_left = left_value <= right_value

        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


def merge_sort_rec(df, column, descending=False):
    ''' merge sort dataframe recursively, returns sorted DataFrame'''
    
    def sort(order):

        if len(order) <= 1:
            return order

        mid = len(order) // 2
        left = sort(order[:mid])
        right = sort(order[mid:])

        return merge_sort(df, column, left, right, descending)

    order = sort(list(range(len(df))))

    #return DataFrame sorted
    return df.iloc[order].copy()


def merge_sort_iter(df, column, descending=False):
    '''merge sort dataframe iteratively (using position in the row instead of a value), returns sorted DataFrame'''
    
    order = list(range(len(df)))

    n = len(order)

    width = 1

    while width < n:

        for start in range(0, n, 2 * width):

            mid = start + width
            end = start + 2 * width

            order[start:end] = merge_sort(
                df, column, order[start:mid], order[mid:end], descending
            )

        width *= 2

    #return DataFrame sorted
    return df.iloc[order].copy()


# ---------------------------------------------------------------------------
# 4. QUICK SORT
# ---------------------------------------------------------------------------

def _quick_partition(df, column, order, low, high, descending):
    """Three-way partition of DataFrame row positions."""
    pivot_position = (low + high) // 2
    pivot_value = df.iloc[order[pivot_position]][column]

    left = low
    current = low
    right = high

    while current <= right:
        current_value = df.iloc[order[current]][column]

        comes_before = (
            current_value > pivot_value
            if descending
            else current_value < pivot_value
        )

        comes_after = (
            current_value < pivot_value
            if descending
            else current_value > pivot_value
        )

        if comes_before:
            order[left], order[current] = (
                order[current],
                order[left]
            )
            left += 1
            current += 1

        elif comes_after:
            order[current], order[right] = (
                order[right],
                order[current]
            )
            right -= 1

        else:
            # Equal to the pivot
            current += 1

    return left, right


def quick_sort_rec(df, column, descending=False):
    """Return a recursively quick-sorted copy of a DataFrame."""
    order = list(range(len(df)))

    def quick_sort(low, high):
        if low >= high:
            return

        equal_start, equal_end = _quick_partition(
            df,
            column,
            order,
            low,
            high,
            descending
        )

        quick_sort(low, equal_start - 1)
        quick_sort(equal_end + 1, high)

    quick_sort(0, len(order) - 1)

    return df.iloc[order].copy()


def quick_sort_iter(df, column, descending=False):
    """Return an iteratively quick-sorted copy of a DataFrame."""
    order = list(range(len(df)))

    if len(order) <= 1:
        return df.copy()

    stack = [(0, len(order) - 1)]

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        equal_start, equal_end = _quick_partition(
            df,
            column,
            order,
            low,
            high,
            descending
        )

        if low < equal_start - 1:
            stack.append((low, equal_start - 1))

        if equal_end + 1 < high:
            stack.append((equal_end + 1, high))

    return df.iloc[order].copy()



# ---------------------------------------------------------------------------
# 5. BINARY SEARCH
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





if __name__ == "__main__":
    print(f"{sys.argv[0]} : Is intended to be imported and not executed.")
