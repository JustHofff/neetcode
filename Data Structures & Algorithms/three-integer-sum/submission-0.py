class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[l], nums[i], nums[r]])

                    curr_l = nums[l]
                    while l < r and nums[l] == curr_l:
                        l += 1
                    curr_r = nums[r]
                    while l < r and nums[r] == curr_r:
                        r -= 1
                elif s > target:
                    r -= 1
                else:
                    l += 1

        return res
