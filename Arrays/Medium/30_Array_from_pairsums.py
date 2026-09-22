def constructArr(self, arr):
    m = len(arr)

    # Special case: only one pair sum means
    # the original array had 2 elements.
    if m == 1:
        return [1, arr[0] - 1]

    # Find n such that:
    # n * (n - 1) // 2 = m
    n = 2

    while n * (n - 1) // 2 < m:
        n += 1

    # If m cannot represent all pairs of an n-sized array
    if n * (n - 1) // 2 != m:
        return []

    res = [0] * n

    # arr[0]   = res[0] + res[1]
    # arr[1]   = res[0] + res[2]
    # arr[n-1] = res[1] + res[2]
    #
    # So:
    # 2 * res[0] = arr[0] + arr[1] - arr[n-1]

    value = arr[0] + arr[1] - arr[n - 1]

    # Must divide evenly by 2
    if value % 2 != 0:
        return []

    res[0] = value // 2

    # First n-1 values of arr are:
    # res[0]+res[1], res[0]+res[2], ...
    for i in range(1, n):
        res[i] = arr[i - 1] - res[0]

    return res

# Time Complexity: O(n)
# Space Complexity: O(n)