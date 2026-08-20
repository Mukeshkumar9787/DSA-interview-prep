class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = defaultdict(int);
        nums_set = set(nums);
        res = 0;
        for num in nums:
            if num - 1 in nums_set:
                continue;
            cache[num] = 1;
            curr = num + 1;
            while(curr in nums_set):
                cache[num] += 1;
                curr += 1;
            res = max(res, cache[num]);
        return res;