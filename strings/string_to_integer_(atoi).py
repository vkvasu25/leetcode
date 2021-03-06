"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

"""

import re

class Solution(object):
    # solution with using regex
    def myAtoi(self, str):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        stripped_str = re.findall('(^[\+\-0]*\d+)\D*', str.strip())

        try:
            result = int(stripped_str[0])
            # print(result)
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0


    # # ugly O(n) solution, needs to check what others did
    # def myAtoi(self, str):
    #     """
    #     :type str: str
    #     :rtype: int
    #     """
    #     result = ""
    #     negative = 0
    #     MAX_INT = 2147483647
    #     MIN_INT = -2147483648
    #     str = str.strip()
    #     if len(str) < 1:
    #         return 0
    #     numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    #     if str[0] == "-":
    #         negative = 1
    #         str = str[1:]
    #         # str = str.replace("-", "") !!!!! this will not work if we have
    #         # input like "--------234" all - will be replaced we should take care
    #         # only of first
    #     elif str[0] == "+":
    #         str = str[1:]
    #         # print('got the +')
    #         # str = str.replace("+", "") !!!!! this will not work if we have
    #         # input like "--------234" all + will be replaced we should take care
    #         # only of first
    #     # print(str)
    #     for i in str:
    #         # print(i)
    #         if i in numbers:
    #             result += i
    #         else:
    #             break
    #     # print(result)
    #     if len(result) > 0:
    #         if int(result) > 2**31-1 and not negative:
    #             return MAX_INT
    #         elif int(result) > 2**31-1 and negative:
    #             return MIN_INT
    #         return int(result) if not negative else -int(result)
    #     return 0


solution = Solution()
print(solution.myAtoi("    42"))
print(solution.myAtoi("    -42"))
print(solution.myAtoi("words and 987"))
print(solution.myAtoi("-91283472332"))
print(solution.myAtoi("91283472332"))
print(solution.myAtoi("+1"))
print(solution.myAtoi(" ++1"))