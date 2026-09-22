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

        '''

        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 1
        return False
