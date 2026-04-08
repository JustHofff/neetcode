class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - 97] += 1

            t = tuple(arr)

            if t not in h:
                h[t] = []
            h[t].append(i)
        
        return list(h.values())