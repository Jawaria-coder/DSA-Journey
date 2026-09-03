def findSplit(self, arr):
    # Return an array of possible answer, driver code will judge and return true or false based on
    total_sum = sum(arr)
    curr_sum = 0
    res = []

    if total_sum % 3 != 0:
        res = [-1, -1]
        return res

    target = total_sum // 3

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == target:
            curr_sum = 0
            res.append(i)


        if len(res) == 2 and i < len(arr) -1:
            return res


    res = [-1, -1]
    return res

# Time : O(n)
# Space: O(1)