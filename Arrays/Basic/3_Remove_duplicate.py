def removeDuplicates(self, arr):
        
    if not arr:
        return 0

    j = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j +=1

    return arr[:j]

# Time : O(n)
# Space: O(1)