"""
--CODEWARS--

TASK :
Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive perfect squares, and return these squares as a string in the format "bigger-smaller"

Examples
9  -->  "25-16"
5  -->  "9-4"
7  -->  "16-9"
"""
import math
def find_squares(num):  
    m = (num-1)//2
    return str((m+1)**2) +"-" +str(m**2)
    
            
