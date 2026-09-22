def findEquilibrium(self, arr):
        
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - arr[i] - left_sum

        if right_sum == left_sum:
            return i

        left_sum += arr[i]

    return -1

# Time : O(n)
# Space: O(1)