def pushZerosToEnd(self, arr):
    left =0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[left], arr[i] = arr[i], arr[left]
            left +=1
            
    return arr

# Time : O(n)
# Space: O(1)