class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        - k is the number of most frequent elements within the array
        - so if k = 2 there are at least two elements with a high frequency
        - gathering each element and their frequencies
        - returning top k frequent elements

        Planning:
        1. create a num freq dict
        2. iterate through nums and get the elements and their frequencies
            if num in dict: dict[num] += 1, else: dict[num] = 1
        3. return top k elements(is there a way to sort the dict)
            create an empty arr list to sort elements and their freq onto
            sort the arr list to have from most to least elements and values
            create an empty res list
            pop k elements and append to res list
            return res list
            
                
        '''
        count = {} #to count the occurences of each value

        # O(n)
        for n in nums: 
            count[n] = 1 + count.get(n,0) #count n in count dict default to 0 + 1 if not in dict

        # O(m)
        arr = []
        for n, c in count.items(): 
            arr.append([c,n])
        # O(m log m)
        arr.sort()

        res = []
        # O(k)
        while len(res) < k:
            res.append(arr.pop()[1]) #arr.pop() removes last elemet of arr where (c,n) = ([0][1]), [1] to get the number
        return res