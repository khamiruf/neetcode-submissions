class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() <= 0 && t.length() <= 0) {
            return true;
        }
        if ((s.length() >0 && !(t.length() >0)) || !(s.length() > 0 && (t.length() > 0))) {
            return false;
        }
        Map<Character, Integer> charCounts = new HashMap<>();

        char[] sArray = s.toCharArray();
        for (Character ch: sArray) {
            charCounts.put(ch, charCounts.getOrDefault(ch, 0) + 1);
        }

        char[] tArray = t.toCharArray();
        for (Character tch: tArray) {
            if (!charCounts.containsKey(tch)){
                return false;
            } 
            if (charCounts.get(tch) == 0) {
                return false;
            }

            charCounts.put(tch, charCounts.get(tch) -1);
        }

        // loop through the hashmap and check if all 0
        for (Integer counts: charCounts.values()) {
            if (counts != 0) {
                return false;
            }
        }

        return true;
    }
}
