class Solution:
    '''
    Understanding: 
    - to encode a list of strings -> string
    - need to be able to go from list of strings -> string -> list of strings
    - Hello World -> join and convert to their ascii characters -> split and decode

    Planning encode: 
    1. if the input list is empty, then it will return an empty string
    2. create an empty list to store sizes of each string
    3. for each string append its length to the sizes list
    4. create a single string by
        writing all sizes seperated by commas
        adding a # to mark the end of a size section
        appending all the actual strings in order
    5. return the final encoded string


    planning decode: 
    1. if the encode string is empty return empty list
    2. read chars from start until reaching # to extract all recorded sizes
        parse each size by reading until a comma
    3. after the #, extract substrings according the the sizes list
        for each size read that many characters and append the substring to the result
    4. return the list of decoded strings
    '''
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], []

        for s in strs: 
            sizes.append(len(s))

        for sz in sizes: 
            res.append(str(sz))
            res.append(',')

        res.append('#')
        res.extend(strs)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if not s: 
            return []

        sizes, res, i = [], [], 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1

        for sz in sizes: 
            res.append(s[i:i+sz])
            i += sz
        return res