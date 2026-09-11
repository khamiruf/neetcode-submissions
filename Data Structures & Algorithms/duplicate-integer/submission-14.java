class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (Integer n: nums) {
            System.out.println(n);
            if (seen.contains(n)) {
                return true;
            }
            seen.add(n);
        }
        return false;
    }
}