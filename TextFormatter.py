# -*- coding: UTF-8 -*-

def formatMultiline(text, line_length):
    return "\n".join(text[i - line_length: i] for i 
                        in range(line_length,
                                 len(text) + line_length,
                                 line_length)
                    )

def breakByWords(text, max_len):
    result = ""
    words = text.split()

    while len(words):
        wordsInLine = len(words)
        while sum(len(word) for word in words[0:wordsInLine]) > max_len:
            wordsInLine = wordsInLine - 1

        if wordsInLine == 0:
            wordsInLine = 1

        result += " ".join(words[0:wordsInLine]) + "\n"
        del words[0:wordsInLine]

    return result