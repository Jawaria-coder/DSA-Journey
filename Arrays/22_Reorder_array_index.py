def reorderArray(arr, index):

    # Pair each element with its target index
    paired = []

    for i in range(len(arr)):
        paired.append([index[i], arr[i]])

    # Sort the pairs by index
    paired.sort()

    # Rearrange arr based on sorted pairs
    for i in range(len(arr)):
        arr[i] = paired[i][1]

    return arr

# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the paired list



## Cycle Sort Approach
def reorderArrayCycle(arr, index):
    i = 0

    while i < len(arr):
        if index[i] != i:
            target = index[i]

            arr[i], arr[target] = arr[target], arr[i]
            index[i], index[target] = index[target], index[i]
        else:
            i += 1

    return arr

# Time Complexity: O(n)
# Space Complexity: O(1)