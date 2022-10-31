package com.enigmagpt.learning.leetcode.algo;

import java.util.Map;
import java.util.Stack;

public class RomanToInteger {

    static class Solution {
        public int romanToInt(String s) {

            final Map<Character, Integer> charMap = Map.of(
                    'I', 1,
                    'V', 5,
                    'X', 10,
                    'L', 50,
                    'C', 100,
                    'D', 500,
                    'M', 1000
            );

            int sum = 0;

            boolean skipNext = false;
            char[] charArray = s.toCharArray();

            for (int i = 0; i < charArray.length; i++) {

                if (skipNext) {
                    skipNext = false;
                    continue;
                }

                int currentNumber = charMap.get(charArray[i]);

                if (i + 1 < charArray.length) {
                    int nextNumber = charMap.get(charArray[i + 1]);

                    if (currentNumber >= nextNumber) {
                        sum += currentNumber;
                    } else {
                        sum += nextNumber - currentNumber;
                        skipNext = true;
                    }

                } else {
                    sum += currentNumber;
                }
            }

            return sum;
        }
    }
}