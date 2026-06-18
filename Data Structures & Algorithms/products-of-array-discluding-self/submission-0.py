class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Understanding: 
        - 48 = 2 * 4 * 6, without first index
        - 24 = 1 * 4 * 6, without second index
        - 12 = 1 * 2 * 6, without third index
        - 8 = 1 * 2 * 4, without fourth index

        Planning: 
        - have a current index pointer to avoid during product operation
        - continue product operation as long as current index pointer is not last index
        - [1,2,4,6], moving pointer to keep a product varible going 
        - in the loop we keep adding factors to the product variable and continue if element is current index
        - append product to output list and set product back to zero to continue to new product operation

        '''


        output = []
        i=0
        j=0
        
        while i != len(nums):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    j+=1 
                    continue
                product *= nums[j]
                j+=1
            output.append(product) 
            i+=1
        return output