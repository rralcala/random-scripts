# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

import sys
def maxProfit(prices):
    return _maxProfit(prices, len(prices) - 1, 0, 0)


def _maxProfit(prices, depth, have, profit):
    if depth == 0:
        return profit
    ret1 = 0#-sys.maxsize - 1
    ret2 = 0 #-sys.maxsize - 1
    if have == 0:
        ret1 = _maxProfit(prices, depth - 1, prices[depth], profit)
    elif prices[depth] >= have:
        ret2 = _maxProfit(prices, depth - 1, 0, prices[depth] - have + profit)

    ret3 = _maxProfit(prices, depth - 1, have, profit)
    #print("{} {} {}".format(ret1, ret2, ret3))
    return max(ret1, ret2, ret3)

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([100,1,100,1,1,1]))