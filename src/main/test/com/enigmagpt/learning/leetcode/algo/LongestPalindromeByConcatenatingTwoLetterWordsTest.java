package com.enigmagpt.learning.leetcode.algo;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class LongestPalindromeByConcatenatingTwoLetterWordsTest {

    @Test
    void test1() {

        LongestPalindromeByConcatenatingTwoLetterWords.Solution solution = new LongestPalindromeByConcatenatingTwoLetterWords.Solution();
        String[] arr = {"ab","ty","yt","lc","cl","ab"};
        int i = solution.longestPalindrome(arr);

        Assert.assertEquals(8, i);
    }

    @Test
    void test2() {

        LongestPalindromeByConcatenatingTwoLetterWords.Solution solution = new LongestPalindromeByConcatenatingTwoLetterWords.Solution();
        String[] arr = {"ty","yt","lc","cl","ab"};
        int i = solution.longestPalindrome(arr);

        Assert.assertEquals(8, i);
    }

    @Test
    void test3() {

        LongestPalindromeByConcatenatingTwoLetterWords.Solution solution = new LongestPalindromeByConcatenatingTwoLetterWords.Solution();
        String[] arr = {"ty","yt","lc","cl","aa", "bb"};
        int i = solution.longestPalindrome(arr);

        Assert.assertEquals(10, i);
    }

    @Test
    void test4() {

        LongestPalindromeByConcatenatingTwoLetterWords.Solution solution = new LongestPalindromeByConcatenatingTwoLetterWords.Solution();
        String[] arr = {"lc", "cl"};
        int i = solution.longestPalindrome(arr);

        Assert.assertEquals(4, i);
    }
}