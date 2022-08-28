class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:

        ySize = len(mat)
        xSize = len(mat[0])

        print("ySize = ", ySize)
        print("xSize = ", xSize)

        for x in range(0, xSize):
            print("---------> X = ", x)
            y = 0
            xx = x
            arr = []
            while xx < xSize and y < ySize:

                arr.append(mat[y][xx])

                xx += 1
                y += 1

            arr.sort()
            print(arr)

            y = 0

            while x < xSize and y < ySize:

                mat[y][x] = arr.pop(0)

                x += 1
                y += 1
        print(mat)

        for y in range(1, ySize):
            x = 0
            yy = y
            arr = []
            print("---------> Y = ", y)
            while x < xSize and yy < ySize:

                arr.append(mat[yy][x])

                x += 1
                yy += 1

            arr.sort()

            x = 0

            while x < xSize and y < ySize:

                mat[y][x] = arr.pop(0)

                x += 1
                y += 1

        print(mat)


Solution.diagonalSort(Solution, [[3,3,1,1],[2,2,1,2],[1,1,1,2]])