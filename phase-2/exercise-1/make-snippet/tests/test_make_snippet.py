from lib.make_snippet import make_snippet
import pytest

@pytest.mark.parametrize('string, expected_result', [
    ('This is a very long sentence', 'This is a very long...'),
])
def test_make_snippet_returns_a_string_of_five_words_and_ellipses(string, expected_result):
    result = make_snippet(string)