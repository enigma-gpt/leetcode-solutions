package com.enigmagpt.learning.leetcode.algo;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {

    static class Solution {

        public List<List<Integer>> generate(int numRows) {

            List<List<Integer>> ret = new ArrayList<>();
            ret.add(List.of(1));

            for (int i = 1; i < numRows; i++) {

                List<Integer> prevSublist = ret.get(i-1);

                List<Integer> newSubList = new ArrayList<>();

                for (int j = 0; j <= prevSublist.size(); j++) {
                    if (j==0 || j == prevSublist.size()) {
                        newSubList.add(1);
                    } else {
                        newSubList.add(prevSublist.get(j-1) + prevSublist.get(j));
                    }
                }
                ret.add(newSubList);
            }

            return ret;
        }
    }
}
