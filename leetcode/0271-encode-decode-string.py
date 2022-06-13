from typing import List


def encode(strs: List[str]) -> str:
    """Encodes a list of strings to a single string.

    Args: 
        strs: A list of strings
    
    Returns:
        a single string with len(word1)#word1len(word2)#word2 format

    dummy_input = ["Hello","World"] 
    res = encode(dummy_input)
    '5#Hello5#World'
    """

    res = ""

    for s in strs:
        res += str(len(s)) + "#" + s
    
    return res
        

def decode(s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """

    res = []
    i = 0
    n = len(s)

    while i < n:
        j = i # j reads up until # 
        while s[j] != '#':
            j += 1

        # the word length (the int portion)
        length = int(s[i:j])

        # the word portion gets extracted and appended into res
        res.append(s[j+1: j+1+length])

        # i points to the int portion of next word
        i = j + 1 + length

    return res
