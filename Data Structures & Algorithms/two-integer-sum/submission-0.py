class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - finding indicies in where nums[i] + nums[j] == target
        - we may assume every input has exactly one pair of indicies i and j
        - target 7, look through array and find values i + j = 7
        - i =  7 - j or j = 7 - i

        - dict, to keep track of numbers already seen in array
        - to see if a difference value gives us target value

        nums: 3,4,5,6   target: 7
        7 - 3 = 4 and 
        if 4 is in nums, return current index and index of 4

        '''

        indexDict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in indexDict: 
                return [indexDict[diff], i]
            else: 
                indexDict[num] = i