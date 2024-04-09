#!/usr/bin/python3
"""
This is the "5-test_indentation" module with one function, text_indentation(text).
"""


def text_indentation(text):
    """Splits a text into lines along '?', ':', '.' followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    lines = []
    line = ''
    for char in text:
        line += char
        if char in ('?', '.', ':'):
            lines.append(line.strip())
            lines.append('\n\n')
            line = ''
    
    # If there's remaining text after the last punctuation, add it to the lines
    if line:
        lines.append(line.strip())
    
    # Print the lines with appropriate indentation
    for line in lines:
        print(line, end='')
