from typing import List


def longestConsecutive(nums: List[int]) -> int:
    set_sequence = set(nums)
    longest = 0

    for num in nums:

        # if num - 1 in the set_sequence, then num is not beginning
        # of a sequence. 
        if (num - 1) in set_sequence:
            continue

        # i is the beginning of a sequence,
        # length increment from 0, 1, 2, 3, ...., until i+length not in sequence
        length = 0
        while (num + length) in set_sequence:
            length += 1
        
        # only the longest length is kept.
        longest = max(length, longest)

    return longest

def main():
    print(f'longest sequence length is : {longestConsecutive(nums = [100,4,200,1,3,2])}')
    print(f'longest sequence length is : {longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])}')


if __name__ == "__main__":
    main()
