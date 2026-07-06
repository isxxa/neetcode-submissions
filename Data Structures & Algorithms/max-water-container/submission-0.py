class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Understanding:
        - trying to find the max amount that can be held between two heights 
        - probably have to keep a max amount held variable going within an operation
        - the element in the ith element has the height of the bar
        - need to use two different pointers to determine the area = length * height

        Intuition: 
        - using two pointers we can search for the max area withoug going through every pair
        - starting with the widest containter (left most to right most)
        - Height will always be limited by the shorter bar/ height, so to potentially get a larger area, 
            we need to move the pointer pointed at the smaller height inward. 
        
        Planning: 
        1. initialize two pointers
            - left = 0
            - right = len(heights)-1
        2. set result = 0 to store the maximum area
        3. while left < right: 
            - compute the current area
            - area = min(heights[left], heights[right]) * (right - left)
            - update res with the maximum area so far
            - move the pointer at the shorter height
                - if heights[left] <= heights[right], move left += 1
                - otherwise move right -= 1
        4. return result after the pointers meet
        ''' 
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            res = max(res, area)
            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1
        return res


