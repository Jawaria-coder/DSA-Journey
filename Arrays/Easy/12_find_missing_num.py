
## Sum of n numbers formula: n(n+1)/2
def missingNum(self, arr):

    full_size = len(arr) +1
    total_sum = sum(arr)

    expected_sum = (full_size * (full_size +1)) // 2

    return expected_sum - total_sum

# Time : O(n)
# Space: O(1)
        

## XOR version
def missingNumXOR(self, arr):

    full_size = len(arr) +1
    res = 0

    for i in range(1, full_size + 1):
        res ^= i

    for x in arr:
        res ^= x

    return res

# Time : O(n)
# Space: O(1)