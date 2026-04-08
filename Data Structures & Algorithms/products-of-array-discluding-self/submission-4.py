class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        for i in range(l):
            if i != 0:
                pre[i] = pre[i - 1] * nums[i - 1]
        
        suf = [1] * l
        for i in range(l - 1, -1, -1):
            if i != l - 1:
                suf[i] = suf[i + 1] * nums[i + 1]
        
        ans = []
        for i in range(l):
            ans.append(pre[i] * suf[i])

        return ans