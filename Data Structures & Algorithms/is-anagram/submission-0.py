class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)

        if len(s) != len(t):
            return False

        for char in a:
            if char in b:
                b.remove(char)
            else:
                return False
        
        return True



    