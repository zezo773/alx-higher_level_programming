#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buf = ""
    for char in text:
        buf += char
        if char in ".?:":
            print(buf.strip())
            print()
            buf = ""
    if buf:
        print(buf.strip())
