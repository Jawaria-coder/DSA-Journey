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