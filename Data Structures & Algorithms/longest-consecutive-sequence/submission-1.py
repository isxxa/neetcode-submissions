class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Understanding: 
        - What is a consecutive sequence: 
            sequence of elements in which each element is exactly 1> than the previous element
        - needs to be written in o(n) cant use nlogn sort function
        - return the length of the longest sequence

        2,3,4,5 
        20
        4
        10

        0,1,2,3,4,5,6
        - its like solitare where we find the longest consecutive number

        - turn the list to a set for easy o(1) lookup
        - storing the length of consectuive numbers
        - starting a new streak whenever count is out of order
        - update the length to new streak
        - returning the length after checking all the numbers 
         

        Planning: 
        1. convert the list nums to a set
        2. create a length variable to store the max streak length
        3. for each number num in list
            - start new streak count at 0
            - set curr = num
            - while curr exist in the set
                - increase the streak count
                - move to the next number curr += 1
            - update length with the longest streak found so far
        4. return length after checking all numbers
        '''

        length = 0
        store = set(nums)

        for num in nums:          
            streak = 0           # if (num-1) not in store:
            curr = num           #   longest = 1
            while curr in store: # while (num + longest) in store:
                streak += 1      #   longest += 1   
                curr += 1
            length = max(length, streak) # length = max(longest, length)

        return length








