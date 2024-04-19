class Solution(object):
    def isAnagram(self, s, t):
        # if length is not the same it is never a anagram
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count characters in s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Subtract character in count based on t
        for char in t:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False
        
        return True