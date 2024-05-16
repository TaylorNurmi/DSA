#About 2 minutes for this solution, I tried without using strings and couldn't quit get it

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        y= x[::-1]
        if int(x)-int(y) == 0: 
            return True