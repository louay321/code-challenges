"""
--CODEWARS--

TASK : 
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def snail(snail_map):
    res = []
    while len(snail_map) > 0:
        #temshi ymin
        res += snail_map[0]
        del snail_map[0]
        if len(snail_map) > 0:
            #tahbet louta
            for i in snail_map:
                res += [i[-1]]
                del i[-1]
            #temshi ysar
            if snail_map[-1]:
                res += snail_map[-1][::-1]
                del snail_map[-1]
                #temshi lfou9
                for i in reversed(snail_map):
                    res += [i[0]]
                    del i[0]
    return res  
