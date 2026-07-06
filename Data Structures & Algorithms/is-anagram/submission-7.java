class Solution {
    public boolean isAnagram(String s, String t) {
        // hashmap: <k: v> : <letter: count>
        // count letters in s_string, increase hashmap counts
        // count letters in t_string, decrease the counts
        // iterate through the values in hashmap, if not zero, return false

        HashMap<Character, Integer> letter_counts = new HashMap<>();

        for (char c: s.toCharArray()) {
            letter_counts.put(c, letter_counts.getOrDefault(c, 0) + 1);
        }

        for (char v: t.toCharArray()) {
            if (letter_counts.containsKey(v)) {
                letter_counts.put(v, letter_counts.get(v) - 1);
            } else {
                return false;
            }
        }

        for (Integer i: letter_counts.values()) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}
