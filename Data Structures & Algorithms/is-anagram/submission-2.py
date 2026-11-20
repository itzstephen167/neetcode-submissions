class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result1 = {}
        result2 = {}
        for letter in s:
            if letter in result1:
                result1[letter] += 1
            else:
                result1[letter] = 1
        for let in t:
            if let in result2:
                result2[let] += 1
            else:
                result2[let] = 1
        return result1 == result2
        