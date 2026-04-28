class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        idx_stack = []

        for i, n in enumerate(temperatures):
            while idx_stack and temperatures[idx_stack[-1]] < n:
                idx = idx_stack.pop()
                res[idx] = i - idx

            idx_stack.append(i)
        
        return res
            
                
