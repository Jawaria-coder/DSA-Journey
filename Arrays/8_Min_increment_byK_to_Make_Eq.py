def minOps(self, arr, k):
        # code here
    maxVal = max(arr)
    operations = 0
    
    for i in range(len(arr)):
        if((maxVal - arr[i]) % k) != 0:
            return -1
    
        operations += (maxVal - arr[i]) // k 
        
    return operations

# Time : O(n)
# Space: O(1)