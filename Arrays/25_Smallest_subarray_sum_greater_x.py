def smallestSubWithSum(self, x, arr):
    n = len(arr)
    left =0
    right =0
    window_sum = 0
    min_len = n+1

    for right in range(n):
        window_sum += arr[right]

        while window_sum > x:
            min_len = min(min_len, right - left +1)

            window_sum -= arr[left]
            left += 1

    if min_len == n +1:
        return 0

    return min_len

# Time Complexity: O(n)
# Space Complexity: O(1)