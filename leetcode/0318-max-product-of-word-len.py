from typing import List


def maxProduct(words: List[str]) -> int:
    """A function that return the max value of len(word[i]) * len(word[j])
    given that two words do not share common letter.

    Args:
        words: array of str

    Returns:
        an integer that is the max value of the length of two words that do
        not share common letter. Return 0 if no such two words exist.

    Precondition:
        - 2 <= words.length <= 1000
        - 1 <= words[i].length <= 1000
        - words[i] consists only of lowercase English letters.

    >>> maxProduct(["a","ab","abc","d","cd","bcd","abcd"]) # 'ab', 'cd'
    4

    """
    answer = 0

    # encode each word
    encoded = []
    for word in words:
        encoded.append(encodeWord(word))

    i = 0
    n = len(words)
    # compare each binary encode with every other binary encode, use bitwise
    # AND operator to see if two word have common character.
    while i < n:

        j = i + 1
        while j < n:

            # bitwise comparison of the two encoded
            if encoded[i] & encoded[j] == 0:
                temp = len(words[i]) * len(words[j])  # compute the multiple
                answer = max(answer, temp)  # compare the new multiple with old.

            j += 1
        i += 1

    return answer


def encodeWord(word: str) -> int:
    """Encode string with bitwise operations.

    Turn lowercase string characters to 26-bit binary representation such that
    a   ->  0....01,
    b   ->  0....10,
    ab  ->  0...011,
    z   ->  1.....0,

    >>> encodeWord('a')
    1
    >>> encodeWord('ab')
    3

    Args:
        word: a string made up of lowercase English alphabets [a-z]

    Returns:
        a unique integer form of the binary representation of the word.

    """
    n = 0
    for i in word:
        index = ord(i) - ord('a')
        n |= 1 << index
        # bitwise shift and then OR comparison with n
        # <=> n = n | 1 << index

    return n


if __name__ == '__main__':
    import doctest

    doctest.testmod()
