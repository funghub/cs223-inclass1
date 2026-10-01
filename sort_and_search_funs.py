import sys

# ---------------------------------------------------------------------------
# 1. SELECTION SORT
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
# 2. INSERTION SORT
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

"""
Merge Sort, Quick Sort, and Binary Search
Each algorithm is implemented in both a recursive and an iterative form.
"""


# ---------------------------------------------------------------------------
# 3. MERGE SORT
# ---------------------------------------------------------------------------

def _merge(df, column, left, right, descending):

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

    def sort(order):

        if len(order) <= 1:
            return order

        mid = len(order) // 2
        left = sort(order[:mid])
        right = sort(order[mid:])

        return _merge(df, column, left, right, descending)

    order = sort(list(range(len(df))))

    #return DataFrame sorted
    return df.iloc[order].copy()


def merge_sort_iter(df, column, descending=False):

    order = list(range(len(df)))

    n = len(order)

    width = 1

    while width < n:

        for start in range(0, n, 2 * width):

            mid = start + width
            end = start + 2 * width

            order[start:end] = _merge(
                df, column, order[start:mid], order[mid:end], descending
            )

        width *= 2

    #return DataFrame sorted
    return df.iloc[order].copy()


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

def binary_search_recursive(df, column_name, target, low=0, high=None, descending=False):
    """
    Recursive binary search on a sorted pandas DataFrame column.
    
    Returns the integer position (iloc index) of the matching row, or -1 if not found.
    """
    if high is None:
        high = len(df) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    mid_val = df.iloc[mid][column_name]

    if mid_val == target:
        return mid

    # Flip comparison direction if the DataFrame is sorted descending
    is_less = (mid_val < target) if not descending else (mid_val > target)

    if is_less:
        return binary_search_recursive(df, column_name, target, mid + 1, high, descending)
    else:
        return binary_search_recursive(df, column_name, target, low, mid - 1, descending)


def binary_search_iterative(df, column_name, target, descending=False):
    """
    Iterative binary search on a sorted pandas DataFrame column.
    
    Returns the integer position (iloc index) of the matching row, or -1 if not found.
    """
    low, high = 0, len(df) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = df.iloc[mid][column_name]

        if mid_val == target:
            return mid
        
        # Flip comparison direction if the DataFrame is sorted descending
        is_less = (mid_val < target) if not descending else (mid_val > target)

        if is_less:
            low = mid + 1
        else:
            high = mid - 1

    return -1



if __name__ == "__main__":
    print(f"{sys.argv[0]} : Is intended to be imported and not executed.")
