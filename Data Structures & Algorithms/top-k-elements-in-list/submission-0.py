class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = [];
        counter = defaultdict(int);
        for num in nums:
            counter[num] += 1;
            if num in topK:
                continue;
            elif len(topK) < k:
                topK.append(num);
            for i, j in enumerate(topK):
                if counter[num] > counter[j]:
                    topK[i] = num;
                    break;
        return topK;