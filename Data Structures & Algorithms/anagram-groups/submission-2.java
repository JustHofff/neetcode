class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for (String s : strs) {
            char[] arr = new char[26];
            for (char c : s.toCharArray()) {
                arr[c - 'a']++;
            }
            String key = new String(arr);
            result.putIfAbsent(key, new ArrayList<>());
            result.get(key).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
