class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s);
        tLen = len(t);
        if sLen != tLen:
            return False;
        counter = defaultdict(int);
        for i in range(sLen):
            counter[s[i]] += 1;
            counter[t[i]] -= 1;

        for value in list(counter.values()):
            if value != 0:
                return False;
        
        return True;