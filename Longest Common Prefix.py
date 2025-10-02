class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        Output = ""
        if not strs:
            return Output
        min_length = min(len(s) for s in strs)
        for i in range(min_length):
            current_character = strs[0][i]
            if all(s[i] == current_character for s in strs):
                Output += current_character
            else:
                break
        return Output
