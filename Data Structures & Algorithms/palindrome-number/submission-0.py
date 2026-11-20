class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        reverse = ""
        reverse += string_x[::-1]
        if reverse == string_x:
            return True
        return False       