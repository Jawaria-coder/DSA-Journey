def circularSubarraySum(self, arr):
    total_sum = sum(arr)

    # Kadane for maximum subarray sum
    current_max = arr[0]
    max_sum = arr[0]

    # Kadane for minimum subarray sum
    current_min = arr[0]
    min_sum = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        max_sum = max(max_sum, current_max)

        current_min = min(arr[i], current_min + arr[i])
        min_sum = min(min_sum, current_min)

    # All elements are negative
    if max_sum < 0:
        return max_sum

    circular_sum = total_sum - min_sum

    return max(max_sum, circular_sum)

# Time Complexity: O(n)
# Space Complexity: O(1)