package com.enigmagpt.learning.leetcode.algo;

import java.util.HashMap;
import java.util.Map;

public class LongestPalindromeByConcatenatingTwoLetterWords {

    static class Solution {
        public int longestPalindrome(String[] words) {

            Map<String, Integer> wordCount = new HashMap<>();

            for (String word : words){
                wordCount.merge(word, 1, Integer::sum);
            }

            int palindromeCountRet = 0;
            boolean middle = false;

            for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {

                String key = entry.getKey();
                Integer value = entry.getValue();

                if (key.charAt(0) < key.charAt(1)) {
                    String reversedKey = "" + key.charAt(1) + key.charAt(0);
                    Integer count = wordCount.get(reversedKey);
                    if(count != null) {
                        palindromeCountRet += 2 * Math.min(value, count);
                    }
                }
                else if (key.charAt(0) == key.charAt(1)) {
                    if(value % 2 == 0) {
                        palindromeCountRet += value;
                    } else {
                        palindromeCountRet += value - 1;
                        middle = true;
                    }
                }
            }

            if (middle) {
                palindromeCountRet++;
            }

            return 2 * palindromeCountRet;
        }
    }
}
