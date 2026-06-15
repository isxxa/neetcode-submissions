class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Understanding:
        - given array nums
        - return true if a value appears more than once in the array
        - return false otherwise

        - go through nums and keep track of number already seen 
        - look at past numbers and return true if number repeats
        - dictionary

        Planning: 
        - create a empty dictionary 
        - iterate through array
        - for each num in index i 
        - if num is in dictionary return true else add to dictionary
        - if gone through loop (without returning true)
        - return false
        '''

        seenNums = {}

        for num in nums:
            if num in seenNums: 
                return True
            else: 
                seenNums[num] = 1
        
        return False