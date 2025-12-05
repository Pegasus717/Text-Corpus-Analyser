import unittest
from tcorpus.main_logic import (
    extract_words, find_palindromes, find_anagrams,
    find_frequencies, find_mask_matches, find_phone_numbers
)

class TestLogic(unittest.TestCase):

    def test_extract(self):
        text = "Café café CAT 123!"
        self.assertEqual(extract_words(text), ["cafe", "cafe", "cat"])
    def test_palindrome(self):
        words = ["madam", "cat", "level"]
        out = find_palindromes(words)
        self.assertEqual(out, ["level", "madam"])

    def test_anagram(self):
        words = ["cat", "tac", "act", "dog"]
        out = find_anagrams(words)
        self.assertEqual(out, [["act", "cat", "tac"]])

    def test_freq(self):
        words = ["a", "b", "a"]
        freq = find_frequencies(words)
        self.assertEqual(freq, {"a": 2, "b": 1})



if __name__ == "__main__":
    unittest.main()
