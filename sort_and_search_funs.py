
def selection_sort_iter()
    













#selection_sort_iter()



def function(















#def function()


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


# ---------------------------------------------------------------------------
# DEMO / SELF-TEST
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import random

    sample = [random.randint(-50, 50) for _ in range(15)]
    print("Original array: ", sample)

    print("\n--- Merge Sort ---")
    print("Recursive:", merge_sort_recursive(sample))
    print("Iterative:", merge_sort_iterative(sample))

    print("\n--- Quick Sort ---")
    print("Recursive:", quick_sort_recursive(sample.copy()))
    print("Iterative:", quick_sort_iterative(sample.copy()))

    print("\n--- Binary Search ---")
    sorted_arr = sorted(sample)
    target = sorted_arr[len(sorted_arr) // 2]
    print("Sorted array:", sorted_arr)
    print(f"Searching for {target}")
    print("Recursive index:", binary_search_recursive(sorted_arr, target))
    print("Iterative index:", binary_search_iterative(sorted_arr, target))

    print("\nSearching for a value not in the array (999):")
    print("Recursive index:", binary_search_recursive(sorted_arr, 999))
    print("Iterative index:", binary_search_iterative(sorted_arr, 999))
