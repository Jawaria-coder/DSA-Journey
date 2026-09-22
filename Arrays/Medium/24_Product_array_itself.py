def productExceptSelf(self, arr):
    n = len(arr)
    res = [1] * n

    # First pass:
    # res[i] stores product of everything LEFT of i
    left_product = 1

    for i in range(n):
        res[i] = left_product
        left_product *= arr[i]

    # Second pass:
    # multiply by product of everything RIGHT of i
    right_product = 1

    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= arr[i]

    return res

# Time Complexity: O(n)
# Space Complexity: O(1) (output array does not count as extra space)