class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            word_count = Counter(word)
            for char in count:
                count[char] = min(count[char], word_count[char])
        
        Output = []
        for char in count:
            for i in range(count[char]):
                Output.append(char)
        return Output
