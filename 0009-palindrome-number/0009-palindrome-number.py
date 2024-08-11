class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check for negative number
        if x < 0:
            return False
        # convert integer to string
        s = str(x)
        # check if string reads the same both ways
        return s == s[::-1]
        