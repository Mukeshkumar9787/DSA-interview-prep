class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = nums.copy();
        prev[0] = 1;
        for i in range(1, len(nums)):
            prev[i] = prev[i - 1] * nums[i - 1];
        
        next = nums.copy();
        next[len(next) - 1] = 1;
        for i in range(len(nums)- 2,-1, -1):
            next[i] = next[i + 1] * nums[i + 1];
        
        for i in range(len(nums)):
            nums[i] = prev[i] * next[i];
            
        return nums;