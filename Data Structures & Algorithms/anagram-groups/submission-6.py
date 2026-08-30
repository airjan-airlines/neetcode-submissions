class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sub map should be hashed str, list of anagrams
        sub_map = {}
        for i in range(len(strs)):
            hash_str = hash(tuple(sorted(Counter(strs[i]).items())))
            if hash_str in sub_map:
                sub_map[hash_str].append(strs[i])
            else:
                sub_map[hash_str] = [strs[i]]
        return list(sub_map.values())
