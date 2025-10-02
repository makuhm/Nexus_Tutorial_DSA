class Solution:
    def freqAlphabets(self, s: str) -> str:
        Output = []
        i = 0 
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                num = int(s[i:i + 2])
                Output.append(chr(ord('a') + num - 1))
                i += 3
            else:
                num = int(s[i])
                Output.append(chr(ord('a') + num - 1))
                i += 1
        return "".join(Output)
