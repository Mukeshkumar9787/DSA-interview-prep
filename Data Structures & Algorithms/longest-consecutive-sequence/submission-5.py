class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums);
        res = 0;
        for num in nums:
            if num - 1 in nums_set:
                continue;
            curr = num + 1;
            while(curr in nums_set):
                curr += 1;
            res = max(res, curr - num);
        return res;