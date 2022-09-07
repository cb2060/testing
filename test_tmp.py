def test_join():
    assert join_strings('abc', 'def') == 'abc def'
    assert join_strings('abc', 'def', separator='/') == 'abc/def'


def join_strings(s1, s2, separator=' '):
    """
    >>> join_strings('abc', 'def')
    'abc def'
    """
    return separator.join((s1, s2))
