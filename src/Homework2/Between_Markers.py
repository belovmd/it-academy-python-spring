"""Between Markers.

You are given a string and two markers (the initial one and final). You have
to find a substring enclosed between these two markers. But there are a few
important conditions. This is a simplified version of the Between Markers
mission.
- The initial and final markers are always different.
- The initial and final markers are always 1 char size.
- The initial and final markers always exist in a string and go one after
another.

Example:
between_markers('What is >apple<', '>', '<') == 'apple'

"""


def between_markers(text: str, begin: str, end: str) -> str:
    """Returns substring between two given markers"""
    st_ind = text.index(begin)
    end_ind = text.index(end)
    return text[st_ind + 1:end_ind]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
