package com.enigmagpt.learning.leetcode.algo;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class ToeplitzMatrixTest {

    @Test
    void tt() {

        int[][] ll = {
                {1, 2},
                {2, 2}
        };

        ToeplitzMatrix toeplitzMatrix = new ToeplitzMatrix();

        ToeplitzMatrix.Solution s = new ToeplitzMatrix.Solution();
        boolean ret = s.isToeplitzMatrix(ll);


        Assert.assertEquals(false, ret);
    }

    @Test
    void tt2() {

        int[][] ll = {
                {1, 2, 3, 4},
                {5, 1, 2, 3},
                {9, 5 ,1, 2}
        };

        ToeplitzMatrix toeplitzMatrix = new ToeplitzMatrix();

        ToeplitzMatrix.Solution s = new ToeplitzMatrix.Solution();
        boolean ret = s.isToeplitzMatrix(ll);


        Assert.assertEquals(true, ret);
    }

    @Test
    void isToeplitzMatrixSolutionFromLeetcode() {

        int[][] ll = {
                {1, 2},
                {2, 2}
        };

        ToeplitzMatrix toeplitzMatrix = new ToeplitzMatrix();

        ToeplitzMatrix.Solution s = new ToeplitzMatrix.Solution();
        boolean ret = s.isToeplitzMatrixSolutionFromLeetcode(ll);


        Assert.assertEquals(false, ret);
    }

    @Test
    void isToeplitzMatrixSolutionFromLeetcode2() {

        int[][] ll = {
                {1, 2, 3, 4},
                {5, 1, 2, 3},
                {9, 5 ,1, 2}
        };

        ToeplitzMatrix toeplitzMatrix = new ToeplitzMatrix();

        ToeplitzMatrix.Solution s = new ToeplitzMatrix.Solution();
        boolean ret = s.isToeplitzMatrixSolutionFromLeetcode(ll);


        Assert.assertEquals(true, ret);
    }
}