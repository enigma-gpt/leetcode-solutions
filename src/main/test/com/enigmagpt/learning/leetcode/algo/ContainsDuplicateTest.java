package com.enigmagpt.learning.leetcode.algo;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class ContainsDuplicateTest {

    @Test
    public void test1() {

        ContainsDuplicate.Solution solution = new ContainsDuplicate.Solution();

        int[] input = {1, 2, 4};

        boolean out = solution.containsDuplicate(input);

        Assert.assertFalse(out);

    }

    @Test
    public void test2() {

        ContainsDuplicate.Solution solution = new ContainsDuplicate.Solution();

        int[] input = {1, 2, 4, 2};

        boolean out = solution.containsDuplicate(input);

        Assert.assertTrue(out);

    }

}