class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int a : nums) {
            boolean added = set.add(a);
            if (!added) {
                return true;
            }
        }
        return false;
    }
}