
def selection_sort_iter(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort_recursive(arr, start=0):
    n = len(arr)
    
    # Base case: If the starting index reaches the end of the array
    if start >= n - 1:
        return
    
    # Assume the current position holds the minimum element
    min_idx = start
    
    # Iterate through the unsorted portion to find the actual minimum
    for j in range(start + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    
    # Move minimum element to its correct position
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    
    # Recursively call the function for the next index
    selection_sort_recursive(arr, start + 1)    











#selection_sort_iter()



def function()


















#def function()
