class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split(" ")
        result.reverse()
        for word in result:
            if len(word) > 0:
                return len(word)

    def lengthOfLastWord2(self, s: str) -> int:
        result = s.strip().split(" ")
        return len(result[len(result) - 1])
