# Python script for LeetCode problems
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0  # t的指標
        for char in s:
            # 在 t 中找到 s 的字元
            while t_index < len(t) and t[t_index] != char:
                t_index += 1
            if t_index == len(t):  # 如果已經遍歷完 t 都找不到
                return False
            t_index += 1  # 找到後，繼續檢查下一個字元
        return True