def leaders(self, arr):
    max_num = arr[-1]
    res = []

    res.append(max_num)

    for i in range(len(arr)-2, -1, -1):
        if arr[i] >= max_num:
            max_num = arr[i]
            res.append(arr[i])
                
    res.reverse()
        
    return res

# Time: O(n)
# Space: O(1)