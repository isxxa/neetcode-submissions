class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Understanding: 
        - return a list of sublists that are groups of anagrams
        - anagram ex: cat, act, 
        - each anagram must have the same number of chars in string
        - the char freq must be the same
        - chars do not have to be in the same order

        index 0 = act
        split(strs[0]) = a c t
        check other words in strs index 1: p o t s, (length is not equal)(first check)
        index 2: tops "
        index 3: cat = c a t (length is equal)(are chars the same)

        problem: going through each string would take o(n^2) time. 

        - same chars? is there a way to sort through each string to then see
            if each string in strs match for anagrams
        
        Planning: 
        - iterate through strs, 
        - sort each string to create a key & add the original string to 
        a list mapped to that key in a dict
        - return the values of that dict as the result

        '''
        groupAna = {}

        for word in strs: 
            #create a key that is the same for all anagrams
            key = "".join(sorted(word))
            if key not in groupAna: 
                groupAna[key] = [] #create new anagroup
            groupAna[key].append(word)


        return list(groupAna.values())