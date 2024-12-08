import re

def match_pattern_a(s):
    pattern = r"1[2-3]*"
    return bool(re.fullmatch(pattern, s))

def match_pattern_b(s):
    pattern = r"[1-3]+"
    return bool(re.fullmatch(pattern, s))

def match_pattern_c(s):
    pattern = r"1+2+3+"
    return bool(re.fullmatch(pattern, s))

def match_pattern_d(s):
    pattern = r"[a-zA-z]+"
    return bool(re.fullmatch(pattern, s))

def match_pattern_e(s):
    pattern = r"[a-zA-Z]*\s[a-zA-Z]*\s?[a-zA-Z]?"
    return bool(re.fullmatch(pattern, s))

def match_pattern_f(s):
    pattern = r"[[][0-9]+[0-9]?,?\s?[0-9]?[0-9]?,?\s?[0-9]?[0-9]?[]]"
    return bool(re.fullmatch(pattern, s))

# Test cases
test_cases = {
    "a": ["1", "12", "123", "13", "14", "112"],
    "b": ["1", "12", "123", "13", "0", "124"],
    "c": ["123", "1123", "1112233", "111222333", "113", "223"],
    "d": ["abc", "ABC", "aBc", "123", "abc123", "!@#", " "],
    "e": ["Hello World", "A B C", "abc", "HelloWorld", " "],
    "f": ["[1, 2, 3]", "[5]", "[10, 20, 30]", "[]", "[1, -2, 3]", "[abc]"],
}

# Testing Function
def test_functions():
    for key, cases in test_cases.items():
        func = globals()[f"match_pattern_{key}"]
        print(f"Testing pattern {key.upper()}:")
        for case in cases:
            result = func(case)
            print(f"  Input: {case} => Match: {result}")
        print()

# Run the test function
test_functions()
