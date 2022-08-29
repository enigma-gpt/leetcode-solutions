import collections
import math


class Solution:

    # my solution 39ms -45ms better than 80%
    def reorderedPowerOf2(self, n: int) -> bool:

        power_of_twos = []
        power = 0
        while int(math.pow(2, power)) <= 1000000000:
            power_of_twos.append(int(math.pow(2, power)))
            power += 1

        print(power_of_twos)

        mapByNumberOfDigits = {}
        for elem in power_of_twos:
            lengthOfNumber = len(str(elem))
            if mapByNumberOfDigits.get(lengthOfNumber) is None:
                mapByNumberOfDigits[lengthOfNumber] = [elem]
            else:
                mapByNumberOfDigits[lengthOfNumber].append(elem)

        print(mapByNumberOfDigits)

        lenOfN = len(str(n))

        x = [int(a) for a in str(n)]

        for number in mapByNumberOfDigits[lenOfN]:
            t = [int(a) for a in str(number)]
            print("num: ", x)
            print("power of two: ", t)
            if sorted(t) == sorted(x):
                return True

        return False

    # Solution from Leetcode discussion board 30ms better than 100%
    def reorderedPowerOf2_2(self, N):
        c = collections.Counter(str(N))

        for i in range(30):
            print(1 << i)

        return any(c == collections.Counter(str(1 << i)) for i in range(30))


print("ANS:   ", Solution.reorderedPowerOf2_2(Solution, 46))

print("ANS:   ", Solution.reorderedPowerOf2_2(Solution, 1))

print("ANS:   ", Solution.reorderedPowerOf2_2(Solution, 10))

print("ANS:   ", Solution.reorderedPowerOf2_2(Solution, 8388608))