class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sub map should be sorted str, list of anagrams
        sub_map = {}
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            if string in sub_map:
                sub_map[string].append(strs[i])
            else:
                sub_map[string] = [strs[i]]
        return list(sub_map.values())