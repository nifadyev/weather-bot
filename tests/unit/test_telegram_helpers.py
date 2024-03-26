import pytest
from src.telegram.helpers import escape_reserved_symbols

@pytest.mark.parametrize(
    argnames=('raw_str', 'escaped_str'),
    argvalues=(
        ('1\\2', '1\\\\2'),
        ('lorem_ipsum', 'lorem\\_ipsum'),
        ('* item in unordered list', '\\* item in unordered list'),
        ('[100, 250]', '\\[100, 250\\]'),
        ('(braces)', '\\(braces\\)'),
        ('~98%', '\\~98%'),
        ('`highlight`', '\\`highlight\\`'),
        ('<another braces>', '<another braces\\>'),
        ('#tag', '\\#tag'),
        ('a+b', 'a\\+b'),
        ('-15', '\\-15'),
        ('y=789', 'y\\=789'),
        ('a|b', 'a\\|b'),
        ('{curly braces}', '\\{curly braces\\}'),
        ('12.34', '12\\.34'),
        ('exclamation!', 'exclamation\\!'),
        ('0', '0'),
    ),
    ids=('\\', '_', '*', '[]', '()', '~', '`', '<>', '#', '+', '-', '=', '|', r'{}', '.', '!', 'no escaping')
)
def test_escape_reserved_symbols(raw_str, escaped_str):
    assert escape_reserved_symbols(raw_str) == escaped_str
