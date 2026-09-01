def reverseArray(self, arr):
    left =0
    right = len(arr) -1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left +=1
        right-=1

    return arr
        
# Time : O(n)
# Space: O(1)

# or arr.reverse() or arr[::-1]