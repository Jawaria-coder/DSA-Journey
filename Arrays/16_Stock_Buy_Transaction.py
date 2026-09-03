def maxProfit(self, prices):
    result = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            result += prices[i] - prices[i-1]

    return result

# Time : O(n)
# Space: O(1)