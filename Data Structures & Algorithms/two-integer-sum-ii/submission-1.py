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

        but this solution does not run in o(1) space and thats what we need so 
        - because the array is sorted we can use two pointers to adjust the sum
        - if currend sum is > move the right pointer to make sum smaller
        - if current sum is < move the left pointer to make sum bigger
        - this will let us close in on target sum without checking every pair because index i < index j 
            such that index i + index j = target

        1. initialize two pointers left and right = len(numbers)-1 
        2. while l < r
            - get current sum = numbers[left] + numbers[right]
            - if currsum > target move right pointer
            - if currsum < target move left pointer
            - else return [l+1, r+1] 
        3. if no pair matches return empty list
        '''

        # seen = {}

        # for i in range(len(numbers)): 
        #     diff = target - numbers[i]
        #     if diff in seen:
        #         return [seen[diff]+1, i+1]
        #     seen[numbers[i]] = i
        # return []


        left = 0
        right = len(numbers)-1

        while left<right: 
            currSum = numbers[left] + numbers[right]
            if currSum > target: 
                right -= 1
            elif currSum < target: 
                left += 1
            else: 
                return [left+1, right+1]

        return []


