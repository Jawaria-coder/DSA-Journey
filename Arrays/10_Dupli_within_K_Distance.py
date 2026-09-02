def checkDuplicatesWithinK(self, arr: list[int], k: int) -> bool:
        
    for i in range(len(arr)):
        for j in range(i+1, min(i+k+1, len(arr))):
            if arr[i] == arr[j]:
                return True

    return False

# Time : O(n*k)
# Space: O(1)