class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = new Set();
        for(let i=0; i < nums.length; i++){
            const num = nums[i];
            if(seen.has(num)) return true;
            seen.add(num);
        }
        return false;
    }
}
