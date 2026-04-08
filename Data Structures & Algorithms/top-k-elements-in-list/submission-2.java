class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hash = new HashMap<>();
        for (int i : nums) {
            if (hash.containsKey(i)) {
                hash.replace(i, hash.get(i) + 1);
            } else {
                hash.put(i, 1);
            }
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
