class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complements = new HashMap<>(); // store num: index

        for (int i=0; i<nums.length; i++) {
            int n = nums[i];
            int comp = target - n;
            if (complements.containsKey(comp)) {
                return new int[]{complements.get(comp) ,i};
            } else {
                complements.put(n, i);
            }
        }

        return new int[]{-1,-1};
    }
}
