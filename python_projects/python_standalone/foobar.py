# Cut exactly equal slices of cake for everyone you'll get in big trouble. 

# The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

# To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

# Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution("abcabcabcabc")
# Output:
#     4

# Input:
# solution.solution("abccbaabccbac")
# Output:
#     2


# < 200 chars of given string
# return max equal parts 
# if no substring - 1 equal part

def compute(string, M, lps):
    length = 0
    i = 1
 
    lps[0] = 0
 
    while i < M:
        if string[i] == string[length]: # string[i] = A 
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:           
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
 
def solution(string):

    n = len(string)
    lps = [0] * n
    print (lps)
    compute(string, n, lps)

    length = lps[n-1]
    print(n)
    print(n%(n - length))
    if n > 0 and n%(n-length) == 0:
        return True
    else:
        False
 
txt = ["ABAB"]
n = len(txt)
for i in range(n):
    if solution(txt[i]):
        print ("True")
    else:
        print ("False")

# print(solution("abcabcbc"))