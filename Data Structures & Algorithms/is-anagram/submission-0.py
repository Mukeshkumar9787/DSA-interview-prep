class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s);
        tLen = len(t);
        if sLen != tLen:
            return False;
        sMap = defaultdict(int);
        tMap = defaultdict(int);
        for i in range(sLen):
            sMap[s[i]] += 1;
            tMap[t[i]] += 1;
        return sMap == tMap;