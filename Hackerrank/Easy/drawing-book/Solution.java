import java.io.*;

class DrawingBook {
    /*
     * Complete the 'pageCount' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER n
     * 2. INTEGER p
     */
    public static int pageCount(int n, int p) {
        // Number of turns starting from page 1
        int firstFlip = p / 2;
        
        // Total possible turns in the book minus turns to the target page
        int lastFlip = (n / 2) - (p / 2);
        
        // Return the minimum of the two paths
        return Math.min(firstFlip, lastFlip);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int p = Integer.parseInt(bufferedReader.readLine().trim());

        int result = DrawingBook.pageCount(n, p);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}