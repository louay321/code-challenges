"""
--CODEWARS--

TASK : 
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n % i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0:
            pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
    print(r)
    return r
    
