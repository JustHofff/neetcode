class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i : nums) {
            hash.put(i, hash.getOrDefault(i, 0) + 1);
        }
        int[] out = new int[k];
        for (int i = 0; i < k; i++) {
            int maxFreq = -1;
            int maxKey = -1;
            for (Map.Entry<Integer, Integer> entry : hash.entrySet()) {
                if (entry.getValue() > maxFreq) {
                    maxFreq = entry.getValue();
                    maxKey = entry.getKey();
                }
            }
            out[i] = maxKey;
            hash.remove(maxKey);
        }
        return out;
    }
}
