from typing import List


def plusOne(digits: List[int]) -> List[int]:
        
        # k points the last element in the array
        # carry bit = 0, and equals to 1 if k == 9

        i = len(digits) - 1

        while i >= 0:
            # if digits[i] != 9, then add 1 to digits[i] and return
            if digits[i] != 9:
                digits[i] += 1
                return digits

            else:
                digits[i] = 0

            i -= 1

        # if all digits are 9, then return [1] + [0] * len(digits)
        result = [1] + [0] * len(digits)
        return result


if __name__ == "__main__":
    result = plusOne([8, 9, 9, 9])
    print(result)
    
    result = plusOne([9, 9, 9, 9])
    print(result)

    result = plusOne([9, 9, 9, 1])
    print(result)
