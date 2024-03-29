from lib.make_snippet import make_snippet
import pytest

@pytest.mark.parametrize('string, expected_result', [
    ('This is a very long sentence', 'This is a very long...'),
    ('Return to step 1 and keep going until your program is complete.', 'Return to step 1 and...'),
    ('Refactor if necessary.', 'Refactor if necessary.'),
    ('Test-drive', 'Test-drive'),
    ('Note Test-driving, design, debugging, and pairing are processes. As such, the most effective way to learn for most people is to see someone apply the process, talk it through, and then try it themselves. For this reason, you may find the videos in this sequence particularly useful.', 'Note Test-driving, design, debugging, and...'),
])
def test_make_snippet_returns_a_string_of_five_words_and_ellipses(string, expected_result):
    result = make_snippet(string)
    assert result == expected_result