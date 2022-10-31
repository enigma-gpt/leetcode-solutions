package com.enigmagpt.learning.leetcode.algo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class RomanToIntegerTest {

    @Test
    void convertRomanNumber1() {

        String romanNumber = "MDCCCLXXXIV";

        RomanToInteger.Solution romanToInteger = new RomanToInteger.Solution();

        int i = romanToInteger.romanToInt(romanNumber);

        Assertions.assertEquals(1884, i);
    }





}