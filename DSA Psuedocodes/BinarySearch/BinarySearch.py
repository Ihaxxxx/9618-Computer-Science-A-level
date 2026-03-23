def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid        
        elif arr[mid] < target:
            low = mid + 1    
        else:
            high = mid - 1    

    return -1                


numbers = [3, 7, 12, 18, 25, 31, 42, 56]

target = 25

result = binary_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")