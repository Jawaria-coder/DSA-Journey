def getAlternates(self, arr):  
    res = []

    for i in range(0, len(arr), 2):
        res.append(arr[i])

    return res
            

# Time Complexity: O(n), where n is the number of elements in arr[]. (One loop)
# Auxiliary Space: O(1)