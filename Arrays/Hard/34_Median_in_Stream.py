def getMedian(arr):
    # left = max-heap using negative values
    # right = normal min-heap
    left = []
    right = []

    result = []

    for x in arr:

        # Step 1: put x into the correct half
        if not left or x <= -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        # Step 2: balance the heaps
        if len(left) > len(right) + 1:
            value = -heapq.heappop(left)
            heapq.heappush(right, value)

        elif len(right) > len(left):
            value = heapq.heappop(right)
            heapq.heappush(left, -value)

        # Step 3: calculate median
        if len(left) == len(right):
            median = (-left[0] + right[0]) / 2
        else:
            median = float(-left[0])

        result.append(median)

    return result

# Time Complexity: O(n log n)
# Space Complexity: O(n)