def longestConsecutive(arr):
    max_count = 0
    seen = set(arr)

    for num in arr:
        if num - 1 not in seen:
            count = 1
            next_num = num + 1

            while next_num in seen:
                count += 1
                next_num += 1

            max_count = max(max_count, count)

    return max_count