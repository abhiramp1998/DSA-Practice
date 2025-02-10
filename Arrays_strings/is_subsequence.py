# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


class Solution:
    def isSubsequence(s: str, t: str) -> bool:

        S = len(s)
        T = len(t)
        j = 0

        if s == '': return True
        if S > T: return False

        for i in range(T):
            if s[j] == t[i]:
                if j == S-1:
                    return True
                j += 1
        
        return False
    

        
    
    print(isSubsequence('abc','ahbgdc'))
    print(isSubsequence('axc','ahbgdc'))