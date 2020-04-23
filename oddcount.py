"""
Anthony Lopez
CS 100 2018F Section 005
HW 05, September 24, 2018
"""

lst = [1,2,3,4,5,6,7)

def oddCount(numList):
    count = 0
    for a in numList:
        if a % 2 != 0:
            count = count + 1
    return(count)

print(oddCount(lst))


