from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Args:
        strs: List of words
    """
    hashmap = {}
    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord('a')] += 1

        if tuple(count) in hashmap:
            hashmap[tuple(count)].append(word)
        else:
            hashmap[tuple(count)] = [word]

    res = []
    for value in hashmap.values():
        res.append(value)

    # print(res)
    return res


if __name__ == '__main__':
    groupAnagrams(["ddddddddddg", "dgggggggggg"])
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])
