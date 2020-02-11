"""Between markers_2.

You are given a string and two markers (the initial and final). You have to
find a substring enclosed between these two markers. But there are a few
important conditions:

- The initial and final markers are always different.
- If there is no initial marker, then the first character should be considered
the beginning of a string.
- If there is no final marker, then the last character should be considered
the ending of a string.
- If the initial and final markers are missing then simply return the whole
string.
- If the final marker comes before the initial marker, then return an empty
string.

"""


def between_markers(text: str, begin: str, end: str) -> str:
    st_ind = text.find(begin)
    end_ind = text.rfind(end)
    if st_ind == end_ind == -1:
        return text
    elif st_ind == -1:
        return text[:end_ind]
    elif end_ind == -1:
        return text[st_ind + len(begin):]
    else:
        return text[st_ind + len(begin): end_ind]


if __name__ == '__main__':
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('All tests passed')
