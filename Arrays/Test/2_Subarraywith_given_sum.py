def subarraysWithSum(arr, S):
    left = 0
    window_sum = 0
    res = []

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > S:
            window_sum -= arr[left]
            left += 1

        if window_sum == S:
            res.append(arr[left:right + 1])

    return res