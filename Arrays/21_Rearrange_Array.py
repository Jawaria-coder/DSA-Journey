def rearrange(self, arr):
    i = 0

    while i < len(arr):
        if arr[i] != -1 and arr[i] != i:
            temp = arr[i]

            arr[i] = arr[temp]
            arr[temp] = temp
        else:
            i += 1

    return arr

# Time Complexity: O(n)
# Space Complexity: O(1)