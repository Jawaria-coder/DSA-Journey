def twoSum(arr, target):
    seen = {}

    for current in range(len(arr)):
        num = target - arr[current]

        if num in seen:
            return [seen[num], current]

        seen[arr[current]] = current

    return []