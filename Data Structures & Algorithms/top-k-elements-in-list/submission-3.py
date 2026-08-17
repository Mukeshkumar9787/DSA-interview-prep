class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int);
        for num in nums:
            counter[num] += 1;
        arr = [];
        for num, cnt in counter.items():
            arr.append([cnt, num]);
        arr.sort();
        res = [];
        while len(res) < k:
            res.append(arr.pop()[1]);
        return res;