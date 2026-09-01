def getSubArrays(self, arr):
        
    result = []
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            result.append(arr[start:end+1])
                
        
    return result

# Time: O(n^3)
# Space: O(n^2)

# for start in range(len(arr)):
#     for end in range(start, len(arr)):
#         print(start, end)

# Time: O(n^2)
# Space: O(1)