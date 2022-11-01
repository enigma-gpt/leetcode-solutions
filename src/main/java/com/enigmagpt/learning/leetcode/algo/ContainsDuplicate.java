package com.enigmagpt.learning.leetcode.algo;

import java.util.Arrays;

public class ContainsDuplicate {
    static class Solution {
        public boolean containsDuplicate(int[] nums) {

            Arrays.sort(nums);

            for( int i = 0; i < nums.length; i++) {

                int currentNum = nums[i];

                if (i + 1 < nums.length) {
                    int nextNum = nums[i + 1];
                    if (currentNum == nextNum) {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
