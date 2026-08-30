class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set = Arrays.stream(nums)
                                     .boxed()
                                     .collect(Collectors.toCollection(HashSet::new));
        if (set.size() != nums.length){
            return true;
        }
        return false;
    }
}