"""
LeetCode Problem -> 125. Valid Palindrome
"""


class Problem125:
    """
    Try it Over Here : https://leetcode.com/problems/valid-palindrome/description/
    """

    def __init__(self, test_case: str = "A man, a plan, a canal: Panama"):
        self.test_case = test_case

    def check_valid_palindrome(self) -> bool:
        new_string = ""
        for char in self.test_case:
            if char.isalnum():
                new_string += char.lower()
        return new_string == new_string[::-1]


test_case_1 = Problem125()
test_case_1.check_valid_palindrome()
