package com.enigmagpt.learning.leetcode.algo;

public class ToeplitzMatrix {

    public static class Solution {

        public boolean isToeplitzMatrix(int[][] matrix) {

            int verticalSize = matrix.length;
            int horizontalSize = matrix[0].length;

            if(verticalSize == 1 && horizontalSize == 1) {
                return true;
            }

            int j = 0;
            for (int i = 0; i < verticalSize; i++) {

                int ii = i;
                int jj = j;

                int currentVal = matrix[ii][0];

                while (ii < verticalSize && jj < horizontalSize) {

                    System.out.println(matrix[ii][jj]);

                    if (currentVal != matrix[ii][jj]) {
                        return false;
                    }

                    ii++;
                    jj++;
                }
            }

            if (horizontalSize > 1) {

                for (int x = 0; x < horizontalSize; x++) {

                    int ii = 0;
                    int jj = x;

                    int currentVal = matrix[ii][jj];

                    while (ii < verticalSize && jj < horizontalSize) {

                        System.out.println(matrix[ii][jj]);

                        if (currentVal != matrix[ii][jj]) {
                            return false;
                        }

                        ii++;
                        jj++;
                    }

                }
            }
            return true;
        }

        public boolean isToeplitzMatrixSolutionFromLeetcode(int[][] matrix) {

            for (int i = 0; i < matrix.length - 1; i++ ) {
                for (int j = 0; j < matrix[0].length - 1; j++) {
                    if (matrix[i][j] != matrix[i+1][j+1]) {
                        return false;
                    }
                }
            }
            return true;
        }
    }
}
