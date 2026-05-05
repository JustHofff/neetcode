class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        res = nums[0]

        while l < r:
            mid = (l + r) // 2

            s = (nums[mid] - nums[l]) == (mid - l) 

            res = min(res, nums[mid], nums[l], nums[r])
            
            if s:
                if nums[l] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return res