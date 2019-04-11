import unittest


def match(search_index, pattern_index, search_string, search_pattern, memo):
    # End of string and pattern should match
    if not memo[pattern_index][search_index]:
        if pattern_index == len(search_pattern):
            memo[pattern_index][search_index] = search_index == len(search_string)
        elif search_index == len(search_string):
            # If a pattern ends with n number of "*" it shouldn't matter as * means 0 or more matches
            memo[pattern_index][search_index] = all(char == "*" for char in search_pattern[pattern_index:])
        elif search_pattern[pattern_index] == "*":
            # Two choices are possible on * match
            # 1. We ignore the "*" and move on to the next character in the pattern
            # 2. Or "*" matches with search_string[search_index]
            memo[pattern_index][search_index] = match(search_index, pattern_index + 1, search_string,
                                                      search_pattern, memo) or match(search_index + 1,
                                                      pattern_index, search_string, search_pattern, memo)
        else:
            first_char = search_pattern[pattern_index] in {"?", search_string[search_index]}
            memo[pattern_index][search_index] = first_char and match(search_index + 1, pattern_index + 1,
                                                                     search_string, search_pattern, memo)
    return memo[pattern_index][search_index]


def is_match(s, p):
    result_matrix = [[None]*(len(s)+1) for _ in range(len(p)+1)]
    return match(0, 0, s, p, result_matrix)


class TestSearchPatter(unittest.TestCase):

    def setUp(self):
        self.string = "cb"
        self.pattern = "?b"
        self.negative_pattern = "?c"

    def test_positive(self):
        self.assertTrue(is_match(self.string, self.pattern))

    def test_negative(self):
        self.assertFalse(is_match(self.string, self.negative_pattern))


if __name__ == '__main__':
    unittest.main(verbosity=2)
