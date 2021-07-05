"""
--CODEWARS--

TASK :
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(s):
    n = 0
    x = ""
    for i in s:
        x += i.upper()
        for j in range(n) :
            x += i.lower();
        n+= 1;
        x+="-"
    return x[:-1]
