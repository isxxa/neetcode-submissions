class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Understanding: 
        - the array is unsorted but we need to find 3 distinct numbers that do not repeat and equal to 0
        - if we sort the array we can fix one number and then search for the other two using the two pointer technique
        - sorting will help us skip the duplicates easily and ensures the pointers will increase or decrease the 
        sum in a predictable way

        - for each fixed number a, we place two pointers: 
            - l starts after i
            - r starts at the end
        - if the currsum is too large we move r to reduct
        - if the currsum is too little we move l to increase
        - when the sum is exactly zero we record the triplet and skip dupicates

        plan: 
        1. sort the array
        2. loop through array using index i
        3. let a = nums[i]
        4. if a > 0 break
        5. set two pointers
        6. while l<r do operation
        7. return the list of valid triplets 

        ***NEED TO VISUALIZE CODE FOR A BETTER UNDERSTANDING - ISA***
        '''

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: 
                break
            
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l<r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: 
                        l += 1
        return res


