from typing import List


def plusOne(digits: List[int]) -> List[int]:
        
        # k points the last element in the array
        # carry bit = 0, and equals to 1 if k == 9
        
        k = len(digits) - 1
        carry = 0
        
        while k >= 0:
            # if carry bit is already 1
            if carry == 1 and digits[k] != 9:
                digits[k] += 1
                carry = 0
                return digits
                
            if digits[k] == 9:
                carry = 1
                digits[k] = 0

            else: # k != 9
                digits[k] += 1
                return digits
            
            k -= 1
        
        return [1] + digits

if __name__ == "__main__":
    result = plusOne([8,9, 9, 9])
    print(result)