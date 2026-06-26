class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Understanding: 
        - similar to regular two sum in the way that we are returning two indexes that sum up to target
        - we can use a similar approach and just add one to whatever index we are returning?

        Plan: 
        1. create seen dict for values 
        2. in the loop find the complement of target - num
        3. if num not in seen add to seen, if num in seen return indexes + 1
        '''

        seen = {}

        for i in range(len(numbers)): 
            diff = target - numbers[i]
            if diff in seen:
                return [seen[diff]+1, i+1]
            seen[numbers[i]] = i