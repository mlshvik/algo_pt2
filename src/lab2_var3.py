import math
def findMax(piles):
    maxi = float('-inf')
    n = len(piles)

    for i in range(n):
        maxi = max(maxi, piles[i])
    return maxi

def JackiesBananas(piles, h):
    left, right = 1, max(piles)

    while left <= right:
        middle = (left + right) // 2
        totalHour = calculateTotalHours(piles, middle)
        if totalHour <= h:
            right = middle - 1
        else:
            left = middle + 1
    return left

def calculateTotalHours(piles, k):
    totalHour = 0
    n = len(piles)

    for i in range(n):
        totalHour += math.ceil(piles[i] / k)
    return totalHour

