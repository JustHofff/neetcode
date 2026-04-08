class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        
        ans = sorted(d, key=lambda x : d[x])
        
        return ans[-k:]
