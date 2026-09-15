import heapq

def topKFreq(arr, k):
    # Step 1: count frequencies
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    # Step 2: keep only top k elements
    min_heap = []

    for value, count in freq.items():

        heapq.heappush(min_heap, (count, value))

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: heap has top k,
    # but we need output in highest-frequency order
    result = []

    while min_heap:
        count, value = heapq.heappop(min_heap)
        result.append(value)

    # min-heap gives smallest first, so reverse
    result.reverse()

    return result

# Time Complexity: O(n log k)
# Space Complexity: O(n)