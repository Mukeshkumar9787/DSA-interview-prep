class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0;
        res = 0;
        processed_nums = sorted(list(set(nums)));
        for i in range(len(processed_nums)):
            if i == 0:
                curr += 1;
            elif (processed_nums[i] - processed_nums[i - 1]) == 1:
                curr += 1;
            else:
                curr = 1;
            res = max(curr, res);
        return res;