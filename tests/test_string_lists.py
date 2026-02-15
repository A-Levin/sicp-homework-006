import pytest
from string_lists import chars, join_chars, reverse_string, is_palindrome, remove_vowels, count_words

class TestChars:
    def test_basic(self):
        assert chars('hello') == ['h', 'e', 'l', 'l', 'o']
    def test_empty(self):
        assert chars('') == []
    def test_single(self):
        assert chars('a') == ['a']

class TestJoinChars:
    def test_basic(self):
        assert join_chars(['h', 'i']) == 'hi'
    def test_empty(self):
        assert join_chars([]) == ''
    def test_single(self):
        assert join_chars(['x']) == 'x'

class TestReverseString:
    def test_basic(self):
        assert reverse_string('hello') == 'olleh'
    def test_palindrome(self):
        assert reverse_string('radar') == 'radar'
    def test_empty(self):
        assert reverse_string('') == ''

class TestIsPalindrome:
    def test_true(self):
        assert is_palindrome('radar') == True
    def test_false(self):
        assert is_palindrome('hello') == False
    def test_single(self):
        assert is_palindrome('a') == True
    def test_empty(self):
        assert is_palindrome('') == True
    def test_two_same(self):
        assert is_palindrome('aa') == True
    def test_two_diff(self):
        assert is_palindrome('ab') == False

class TestRemoveVowels:
    def test_basic(self):
        assert remove_vowels('hello') == 'hll'
    def test_all_vowels(self):
        assert remove_vowels('aeiou') == ''
    def test_no_vowels(self):
        assert remove_vowels('xyz') == 'xyz'
    def test_mixed_case(self):
        assert remove_vowels('HeLLo') == 'HLL'

class TestCountWords:
    def test_three(self):
        assert count_words('hello world here') == 3
    def test_single(self):
        assert count_words('word') == 1
    def test_empty(self):
        assert count_words('') == 0
