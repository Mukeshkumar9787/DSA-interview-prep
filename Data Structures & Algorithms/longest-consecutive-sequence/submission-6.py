class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums);
        res = 0;
        for num in nums:
            if num - 1 in nums_set:
                continue;
            inc = 1;
            while(num + inc in nums_set):
                inc += 1;
            res = max(res, inc);
        return res;