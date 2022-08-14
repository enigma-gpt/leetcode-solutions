class Solution:
    def is_palindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if x < 10:
            return True

        x_str = str(x)
        reversed_str = x_str[::-1]
        return int(reversed_str) == x


    def is_palindrome2(self, x: int) -> bool:

        if x < 0:
            return False

        if x < 10:
            return True

        digit_arr = [int(i) for i in str(x)]

        arrLen = len(digit_arr)
        halfArrLen = int(arrLen/2)

        for i in range(0, halfArrLen):
            print("iter = ", i)
            if digit_arr[i] != digit_arr[arrLen - i - 1]:
                return False
        return True


    #final
    def isPalindrome3(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)
        reversed_str = x_str[::-1]
        return int(reversed_str) == x


#False
print(Solution.is_palindrome(Solution, 1234331))

#False
print(Solution.is_palindrome(Solution, 1321))

#True
print(Solution.is_palindrome(Solution, 1))

#True
print(Solution.is_palindrome(Solution, 12321))

#True
print(Solution.is_palindrome(Solution, 1221))

#False
print(Solution.is_palindrome(Solution, -1221))
