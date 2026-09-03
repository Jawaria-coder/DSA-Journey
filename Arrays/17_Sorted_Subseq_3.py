def find3Numbers(self, arr):
        
    first = float('inf')
    second = float('inf')
    first_for_second = 0

    for x in arr:
        if x <= first:
            first = x
        elif x <= second:
            second = x
            first_for_second = first
        else:
            return [first_for_second, second, x]

    return []
