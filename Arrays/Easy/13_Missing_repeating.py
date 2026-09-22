
## Freq + sum of n numbers formula: n(n+1)/2 Approach
def findTwoElement(self, arr):
    count = {}
    arr2 = []
        
    for x in arr:
        count[x] = count.get(x, 0) + 1
        
    for value in arr:
        if count[value] == 2:
            repeated = value
            arr2.append(repeated)
            break
        
    total_sum = sum(arr) - repeated
        
    n = len(arr)
    expected_sum = n * (n + 1) // 2
        
    missing = expected_sum - total_sum
        
    arr2.append(missing)
        
    return arr2

# Time : O(n)
# Space: O(n)

### XOR Approach
def findTwoElementXOR(self, arr):
    # n is the size of the array.
    # Since values should be from 1 to n, the expected numbers are 1, 2, ..., n.
    n = len(arr)

    # This will eventually hold:
    # repeating_number XOR missing_number
    xor_all = 0

    # XOR all values that are actually present in the array.
    # Example:
    # arr = [4, 3, 6, 2, 1, 1]
    #
    # xor_all becomes:
    # 4 ^ 3 ^ 6 ^ 2 ^ 1 ^ 1
    for x in arr:
        xor_all ^= x

    # XOR all numbers that SHOULD be present: 1 to n.
    #
    # Expected:
    # 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6
    #
    # When combined with the array XOR,
    # all normal numbers cancel because:
    # x ^ x = 0
    #
    # Only the repeating and missing numbers remain.
    for i in range(1, n + 1):
        xor_all ^= i

    # At this point:
    # xor_all = repeating ^ missing
    #
    # Example:
    # repeating = 1
    # missing = 5
    #
    # xor_all = 1 ^ 5 = 4
    #
    # In binary:
    # 1 = 001
    # 5 = 101
    # --------
    #     100


    # Find one bit where repeating and missing are different.
    #
    # xor_all & -xor_all gives the rightmost set bit.
    #
    # Example:
    # xor_all = 100
    # set_bit = 100
    #
    # This bit can separate the two numbers into different groups.
    set_bit = xor_all & -xor_all

    # These will hold the XOR results of the two groups.
    group1 = 0
    group2 = 0

    # Split the ACTUAL array into two groups.
    #
    # If a number has set_bit turned ON:
    #     put it in group1
    #
    # Otherwise:
    #     put it in group2
    #
    # We don't physically create lists.
    # We just XOR the values into group1 or group2.
    for x in arr:
        if x & set_bit:
            group1 ^= x
        else:
            group2 ^= x

    # Now do the exact same grouping for the EXPECTED numbers 1 to n.
    #
    # Normal numbers will appear once in the array
    # and once in the expected range.
    #
    # They go into the same group and cancel:
    # x ^ x = 0
    #
    # After all cancellations:
    # one group will contain the repeating number
    # and the other will contain the missing number.
    for i in range(1, n + 1):
        if i & set_bit:
            group1 ^= i
        else:
            group2 ^= i

    # Now group1 and group2 are the two answers,
    # but XOR cannot tell us which one is:
    #
    # repeating
    # missing
    #
    # Example:
    # group1 = 5
    # group2 = 1
    #
    # We need to check the original array.


    # If group1 appears twice in arr,
    # then group1 is the repeating number.
    if arr.count(group1) == 2:
        repeating = group1
        missing = group2

    # Otherwise group2 must be the repeating number.
    else:
        repeating = group2
        missing = group1

    # Problem expects:
    # [repeating, missing]
    return [repeating, missing]
            

# Time : O(n)
# Space: O(1)
        
        
         

