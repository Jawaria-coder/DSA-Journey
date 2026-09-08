def majorityElement(self, arr):
        count = {}

        for x in arr:
            count[x] = count.get(x, 0) + 1

        for value in count:
            if count[value] > len(arr) // 2:
                return value

        return -1

# Time Complexity: O(n)
# Space Complexity: O(n)

### Boyer-Moore Voting Algorithm
def majorityElementBoyerMoore(self, arr):
        count = 0
        candidate = None

        if count == 0:
            candidate = current
            count = 1
        if current == candidate:
            count += 1
        else:
            count -= 1

        occurence = 0
        for num in arr:
            if num == candidate:
                occurence += 1  
        
        if occurence > len(arr) // 2:
            return candidate

            
# Time Complexity: O(n)
# Space Complexity: O(1)