class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        
        for i in range(len(s)):
            if s[i] not in dicS:
                dicS[s[i]] = [i]
            else:
                dicS[s[i]].append(i)
            if t[i] not in dicT:
                dicT[t[i]] = [i]
            else:
                dicT[t[i]].append(i)
            
            if dicS[s[i]] != dicT[t[i]]:
                return False
            
        return True