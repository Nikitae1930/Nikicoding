class Solution {
    public void rotate(int[][] matrix) {
        int temp, i, j;
        for(i = 0; i < matrix.length; i++)
        {
            for(j = i + 1; j < matrix[0].length; j++)
            {
                temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
        int l = 0;
        i = 0;
        int n = matrix.length; 
        while(l < matrix.length){
            for (j = 0; j < n / 2; j++) { 
                temp = matrix[i][j]; 
                matrix[i][j] = matrix[i][n - j - 1]; 
                matrix[i][n - j - 1] = temp; 
            } 
            l++;
            i = l;
        }
    }
}