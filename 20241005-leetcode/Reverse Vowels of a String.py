# Python script for LeetCode problems
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        is_vowels = []

        for char in s:
            if char in vowels:
                is_vowels.append(char)

        is_vowels.reverse()

        vowel_order = 0
        result = []

        for char in s:                                  #  mistake: string 不能直接像 list 一樣可以直接替換
            if char in vowels:
                result.append(is_vowels[vowel_order])
                vowel_order += 1
            else:
                result.append(char)

        return ''.join(result)