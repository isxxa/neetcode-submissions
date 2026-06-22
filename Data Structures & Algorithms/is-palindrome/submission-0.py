class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Understand: 
        - find a way to determine if a string is a palinfrome
        - from the left side and the right side, the numbers and letters need to be equal 
        - if the string does not match at any given point then it is not a palindrome
            and we need to return false
        
        Planning: 
        - we can use isalnum() to determine if char in string s is a letter or number
        - iterate through the string from the left and from the right using pointers 
        - if the chars that the pointers are pointing to do not match we return false
        - if we go through the entire string without finding a mismatch then we return true

        1. initialize left and right pointer
        2. if left and right pointer are not letter or number move inward to next char by 1
        3. if left and right pointer are not equal to each other return false 
        4. if left and right pointer are equal to each other then move inware to next char by 1
        5. if gone through entire array without fail return true at the end after loop 
        '''

        left = 0
        right = len(s) - 1

        while left < right: 
            if not s[left].isalnum(): 
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True