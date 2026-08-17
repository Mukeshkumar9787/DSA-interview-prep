class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = set();
        counter = defaultdict(int);
        for num in nums:
            counter[num] += 1;
            if num in topK:
                continue;
            if len(topK) < k:
                topK.add(num);
                continue;
            for j in topK.copy():
                if counter[num] > counter[j]:
                    topK.remove(j);
                    topK.add(num);
        return list(topK);