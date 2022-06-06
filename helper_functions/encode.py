def encode(word: str) -> int:
    """Each combination of letters should return a unique int.
    
    Args:
        word: the word to encode to integer
    
    Returns:
        An int that represents a combination of chars
    
    >>>
    
    """
    n = 0
    for i in word:
        index = ord(i) - ord('a')
        n |= 1 << index
        print(f'word {word} index: {index} and n: {n}')
        # bitwise shift and then OR comparison with n
        # <=> n = n | 1 << index

    return n


if __name__ == "__main__":
    
    a = encode("ddddddddddg")
    print(a)
    
    b = encode("dgggggggggg")
    print(b)
