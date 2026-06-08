class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join(char for char in s if char.isalnum())

        if check.lower() == check[::-1].lower():
            return True
        else:
            return False