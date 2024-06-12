from __future__ import annotations


def remove_trailing_whitespaces(s: str) -> str:
    """
    Removes trailing whitespaces from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with trailing whitespaces removed.
    """
    lines = s.split("\n")
    stripped_lines = [line.rstrip() for line in lines]
    return "\n".join(stripped_lines)


def remove_trailing_empty_lines(s: str) -> str:
    """
    Removes trailing empty lines from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with trailing empty lines removed.
    """
    return s.rstrip("\n")


def clean_string(s: str) -> str:
    """
    Cleans a string by removing trailing whitespaces and empty lines.

    Args:
        s (str): The input string.

    Returns:
        str: The cleaned string.
    """
    s = remove_trailing_whitespaces(s)
    s = remove_trailing_empty_lines(s)
    return s


def remove_comments(s: str, commenter: str = "#") -> str:
    """
    Removes comments from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with comments removed.
    """
    lines = s.split("\n")
    cleaned_lines = []
    for line in lines:
        if line.lstrip().startswith(commenter):
            continue
        if commenter in line:
            cleaned_lines.append(line.split(commenter)[0])
        else:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def get_last_line(s: str) -> str:
    """
    Gets the last line of a string.

    Args:
        s (str): The input string.

    Returns:
        str: The last line of the string.
    """
    if not s:
        return ""
    lines = s.splitlines()
    return lines[-1]


def starts_with_whitespace(s: str):
    """
    Checks if a string starts with whitespace.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string starts with whitespace, False otherwise.
    """
    if not s:
        return False
    return s[0].isspace()


def get_last_unindent_line(s: str) -> str:
    """
    Gets the last unindent line of a string.

    Args:
        s (str): The input string.

    Returns:
        str: The last unindent line of the string.
    """
    if not s:
        return ""
    lines = s.splitlines()
    for line in reversed(lines):
        if line.startswith((" ", "\t")):
            continue
        return line
    return ""


def get_last_unindent_index(s: str) -> int:
    """
    Gets the last unindent index of a string.

    Args:
        s (str): The input string.

    Returns:
        int: The last unindent index of the string.
    """
    if not s:
        return -1
    lines = s.splitlines()
    for index, line in reversed(list(enumerate(lines))):
        if line.startswith((" ", "\t")):
            continue
        return index
    return -1


def get_str_from_index(s: str, index: int) -> str:
    """
    Gets the string from a given index.

    Args:
        s (str): The input string.
        index (int): The index.

    Returns:
        str: The string from the index.
    """
    if index < 0:
        return ""
    return s[index:]


def remove_new_lines(s: str) -> str:
    """
    Removes new lines from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with new lines removed.
    """
    return s.replace("\n", "").replace("\r", "")


def flatten_str(s: str) -> str:
    """
    Removes new lines, tabs and spaces from a string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with new lines and tabs removed.
    """
    if not s:
        return ""
    lines = s.splitlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return "".join(result)
