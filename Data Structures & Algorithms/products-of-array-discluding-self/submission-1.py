class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        prefix = 1;
        for i in range(len(res)):
            curr = res[i];
            res[i] = prefix;
            prefix = prefix * curr;
        suffix = 1;
        for i in range(len(res) - 1, -1, -1):
            res[i] *= suffix;
            suffix = suffix * nums[i];
        return res;