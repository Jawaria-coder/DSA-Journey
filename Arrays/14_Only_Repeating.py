### Set Approach
def findDuplicate(self, arr):
    seen = set()

    for x in arr:
        if x in seen:
            return x
        seen.add(x)

    return -1
        
# Time : O(n)
# Space: O(n)

### Sum Approach
def findDuplicateSum(self, arr):
    n = len(arr) - 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)

    return actual_sum - expected_sum

# Time : O(n)
# Space: O(1)

### XOR Approach
def findDuplicateXOR(self, arr):
    n = len(arr)
    xor_all = 0

    for x in arr:
        xor_all ^= x

    for i in range(1, n):
        xor_all ^= i

    return xor_all

# Time : O(n)
# Space: O(1)
