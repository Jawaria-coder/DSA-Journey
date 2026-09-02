### Dictionary version
def findUnique(self, arr):
    count = {}

    for x in arr:
        count[x] = count.get(x,0) + 1

    for value in arr:
        if count[value] == 1:
            return value

    return -1

# Time : O(n)
# Space: O(n)

#### XOR version
def findUniqueXOR(self, arr):
    res = 0

    for x in arr:
        res ^= x

    return res

# Time : O(n)
# Space: O(1)

# Only applicable when there is exactly one unique element and all other elements appear exactly twice.