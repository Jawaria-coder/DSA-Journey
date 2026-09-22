def kthLargestSubarraySum(self, arr, k):
    min_heap = []

    for i in range(len(arr)):
        current_sum = 0

        for j in range(i, len(arr)):
            current_sum += arr[j]

            if len(min_heap) < k:
                heapq.heappush(min_heap, current_sum)

            elif current_sum > min_heap[0]:
                heapq.heapreplace(min_heap, current_sum)

    return min_heap[0]