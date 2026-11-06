class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            res+=i if i.isdigit() or i.isalpha() else ""
        temp = res.lower()
        return (temp[::-1]==temp)