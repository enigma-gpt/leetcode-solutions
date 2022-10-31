package com.enigmagpt.learning.leetcode.algo;

public class RomanToInteger {

    static class Solution {
        public int romanToInt(String s) {

            int sum = 0;
            char[] charArray = s.toCharArray();

            int i = 0;
            while (i < charArray.length) {

                int currentNumber = toInt(charArray[i]);

                if (i + 1 < charArray.length) {
                    int nextNumber = toInt(charArray[i + 1]);

                    if (currentNumber >= nextNumber) {
                        sum += currentNumber;
                    } else {
                        sum += nextNumber - currentNumber;
                        i++;
                    }

                } else {
                    sum += currentNumber;
                }

                i++;
            }

            return sum;
        }

        private static int toInt(char c) {

            switch (c) {
                case 'I':
                    return 1;
                case 'V':
                    return 5;
                case 'X':
                    return 10;
                case 'L':
                    return 50;
                case 'C':
                    return 100;
                case 'D':
                    return 500;
                case 'M':
                    return 1000;
            }

            return -1;
        }
    }
}