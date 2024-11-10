class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        ans = 0
        previous_value = 0  

        for char in s[::-1]:  
            current_value = roman_numerals[char]  
            if current_value < previous_value:
                ans -= current_value 
            else:
                ans += current_value  
            previous_value = current_value  

        return ans
