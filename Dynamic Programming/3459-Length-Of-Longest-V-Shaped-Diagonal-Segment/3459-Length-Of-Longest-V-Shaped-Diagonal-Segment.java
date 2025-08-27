class Solution {
    public int[][] rotate(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] newGrid = new int[n][m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                newGrid[i][j] = grid[m - 1 - j][i];
            }
        }
        return newGrid;
    }
    
    public int computeLeftMax(int cell, int prevCell, int prevLeftMax) {
        if (cell == 1) return 0;
        if (cell + prevCell == 2) return prevLeftMax + 1;
        return 1; // cell = 0 or 2
    }
    
    public int computeRightMax(int cell, int prevCell, int prevRightMax) {
        if (cell == 1) return 1;
        if (prevRightMax == 0) return 0;
        if (prevRightMax == 1) {
            if (cell == 2) return 2;
            else return 0;
        }
        if (cell + prevCell == 2) return prevRightMax + 1;
        return 0;
    }
    
    public int lenOfHorizontalVDiagonal(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        int[][] leftMax = new int[m][n];
        int[][] rightMax = new int[m][n];
        int result = 1;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0 && j > 0) {
                    leftMax[i][j] = computeLeftMax(grid[i][j], grid[i - 1][j - 1], leftMax[i - 1][j - 1]);
                } else {
                    if (grid[i][j] == 1) leftMax[i][j] = 0;
                    else leftMax[i][j] = 1;
                }
                
                if (i > 0 && j < n - 1) {
                    rightMax[i][j] = computeRightMax(grid[i][j], grid[i - 1][j + 1], rightMax[i - 1][j + 1]);
                } else {
                    if (grid[i][j] == 1) rightMax[i][j] = 1;
                    else rightMax[i][j] = 0;
                }
                
                if (rightMax[i][j] > 0) {
                    result = Math.max(result, leftMax[i][j] + rightMax[i][j] - 1);
                }
            }
        }
        return result;
    }
    
    public int lenOfVDiagonal(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        boolean oneSeen = false;
        for (int i = 0; i < m && !oneSeen; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    oneSeen = true;
                    break;
                }
            }
        }
        if (!oneSeen) return 0;
        
        int bestResult = 1;
        bestResult = lenOfHorizontalVDiagonal(grid);
        
        for (int i = 0; i < 3; i++) {
            grid = rotate(grid);
            bestResult = Math.max(bestResult, lenOfHorizontalVDiagonal(grid));
        }
        return bestResult;
    }
}
