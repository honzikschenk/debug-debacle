problems = [
    {
        "code": """def twoSum(arr: tuple[list[int], int]) -> list[int]:
    # Finds the indices of two numbers in nums that add up to target
    # The 1st element of arr is nums and the 2nd element of arr is target

    complements = dict()

    nums, target = arr

    for i, num in enumerate(nums):
        if num in complements:
            return [complements[num], i]
        complements[num] = i""",
        "description": "",
        "testCases": ["[[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]", "[[0, 1], [1, 2], [0, 1]]"]
    },
    {
        "code": """def isPalindrome(x: int) -> bool:
    # Checks whether x is a palindrome
    return x == x[::-1]""",
        "description": "",
        "testCases": ["[121, -121, 10]", "[True, False, False]"]
    },
    {
        "code": """def lengthOfLongestSubstring(s: str) -> int:
    # Finds the length of the longest substring without repeating characters
    substring_start = 0
    chars = dict()
    max_length = 0

    for i, ch in enumerate(s):
        if ch in chars:
            substring_start = max(substring_start, chars[ch] + 1)
        chars[ch] = i
        
        length = i - substring_start
        max_length = max(max_length, length)
    
    return max_length""",
        "description": "",
        "testCases": ['["abcabcbb", "bbbbb", "pwwkew"]', "[3, 1, 3]"]
    },
    {"code": """def is_palindrome(s):
        #Checks if a given string is a palindrome, ignoring non-alphanumeric characters and case.
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1][:1]""",
        "description" : "",
        'testCases': ["['racecar', 'A man a plan a canal Panama', 'Was it a car or a cat I saw?', 'Hello world', 'A man and his cow]", '[True, True, True, False, False]']
    },
    {'code': "def findDisappearedNumbers(nums):\n    #The function returns a list describing the numbers from 1 to 10 missing from the given list.\n    n = len(nums)\n    result = []\n    for i in range(1, n):\n        if i not in nums:\n            result.append(i)\n    return result", 
     'description': '', 
     'testCases': ['[[1, 2, 3, 4, 5], [1, 2, 3, 7, 8, 9, 10], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 5, 6]]', '[[6, 7, 8, 9, 10], [4, 5, 6], [2, 3, 4, 5, 6, 7, 8, 9, 10], [], [4, 7, 8, 9, 10]]']
    },
    {'code': 'def largest_triangle_area(points):\n    #The function finds the largest area of a triangle formed by any three points in the given set of points.\n   area = 0\n    for i in range(len(points)):\n        for j in range(i+1, len(points)):\n            for k in range(j+1, len(points)):\n                x1, y1 = points[i]\n                x2, y2 = points[j]\n                x3, y3 = points[k]\n                return max(area, 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) + 1)', 
     'description': '', 
     'testCases': ['[[(0, 0), (0, 3), (4, 0)], [(0, 0), (0, 1), (1, 0)], [(0, 0), (1, 1), (2, 0)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 1), (1, -1)]]', '[6.0, 0.5, 1.0, 0.5, 1.0]']
    },
    {'code': 'def find_missing_number(arr):\n    #This function finds the missing number in a list of consecutive integers.\n    n = len(arr)\n    expected_sum = n * (n + 1) // 2\n    actual_sum = sum(arr)\n    return expected_sum - actual_sum', 'description': '', 
     'testCases': ['[[1, 2, 3, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8, 10, 11], [100, 102, 103, 104, 105, 106, 107, 108, 109], [1, 2, 3, 5], [1, 2, 4, 5, 6]]', '[5, 9, 101, 4, 18]']
     }]