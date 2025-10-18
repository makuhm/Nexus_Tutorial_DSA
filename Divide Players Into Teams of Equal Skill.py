class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        target = skill[left] + skill[right]
        chemistry = 0

        while left < right:
            s = skill[left + 1] + skill[right - 1]
            if s != target:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return chemistry
