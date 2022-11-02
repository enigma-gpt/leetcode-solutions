package com.enigmagpt.learning.leetcode.algo;

import org.junit.jupiter.api.Test;

import java.util.List;

class PascalsTriangleTest {

    @Test
    void test1() {
        PascalsTriangle.Solution solution = new PascalsTriangle.Solution();

        List<List<Integer>> generate = solution.generate(7);

        generate.forEach(sList -> {
            sList.forEach(System.out::println);
            System.out.println(System.lineSeparator());
        });
    }

}