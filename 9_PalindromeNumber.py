class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        original_x = x
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10

        return x == rev or x == rev // 10