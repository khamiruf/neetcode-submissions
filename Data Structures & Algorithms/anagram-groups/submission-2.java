class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Map of sorted string -> list of original anagrams
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            // Sort the string to create the unique key
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedKey = new String(chars);
            
            // Get the list or create a new one, then add the original string
            map.putIfAbsent(sortedKey, new ArrayList<>());
            map.get(sortedKey).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}