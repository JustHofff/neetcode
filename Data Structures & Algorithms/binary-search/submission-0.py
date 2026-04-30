class Solution:
    def bs(self, start: int, end: int, nums: List[int], target: int) -> int:
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.bs(mid + 1, end, nums, target)
        else:
            return self.bs(start, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bs(0, len(nums) - 1, nums, target)