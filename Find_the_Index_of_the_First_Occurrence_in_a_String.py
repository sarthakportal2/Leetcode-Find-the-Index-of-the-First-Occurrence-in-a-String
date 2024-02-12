class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":return i#initalizing needle 

        for i in range(len(haystack)+1-len(needle)):#iterating to both needle and hasystack
            if haystack[i:i+len(needle)]==needle:return i#printing needle's length indx val
        return -1#printing -1
