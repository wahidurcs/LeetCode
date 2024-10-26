class Solution(object):
    def isPalindrome(self,x):
        if x < 0:  
                return False

        original_number = x
        reverse_number = 0
        while x > 0:
            lastdigit = x % 10
            reverse_number = reverse_number * 10 + lastdigit
            x //= 10
        return original_number == reverse_number


   
