import unittest
from tcorpus.main_logic import (
    extract_words, find_palindromes, find_anagrams,
    find_frequencies, find_mask_matches, find_phone_numbers
)

class TestLogic(unittest.TestCase):

    def test_extract(self):
        text = "Café café CAT 123!"
        self.assertEqual(extract_words(text), ["cafe", "cafe", "cat"])

