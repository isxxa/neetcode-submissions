class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        - if strings are not the same length return false
        - each letter in s needs to have the same freq in t
        - keep track of letters in s to compare to t
        - dict
            - add char and count to dict when iterating through string
            - if it comes up again add to letter count
            ex: s = racecar
            dict: r:2, a:2, c:2, e:1
        - iterate through second string t
        - for each letter in t in s substract letter count
        - after loop if letters in dict all equal to zero return True
        - otherwise return false
        '''

        charFreq = {}

        for char in s: 
            if char not in charFreq: 
                charFreq[char] = 1
            else: 
                charFreq[char] += 1

        for char in t: 
            if char in charFreq != 0: 
                charFreq[char] -= 1
            if char not in charFreq:
                return False

        for i in charFreq:
            if charFreq[i] != 0: 
                return False

        return True
