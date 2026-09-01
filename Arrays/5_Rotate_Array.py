class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
    
        if n == 0:
            return
    
        d = d % n
    
        arr[:] = arr[d:] + arr[:d]  ## left rotation

# Time : O(n)
# Space : O(n)

# LEFT rotation
# arr[:] = arr[d:] + arr[:d]

# # RIGHT rotation
# arr[:] = arr[-d:] + arr[:-d]

### Reversal ALGorithm
def rotateArr(arr, d):
    n = len(arr)

    d %= n

    arr.reverse()

    ## Right rotation
    arr[:d] = reversed(arr[:d])

    arr[d:] = reversed(arr[d:])

# Time : O(n)
# Space : O(1)