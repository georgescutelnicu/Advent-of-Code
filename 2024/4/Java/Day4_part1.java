import java.io.*;
import java.util.*;

public class Day4_part2 {
    public static void main(String[] args) {

        List<String> grid = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("4.txt"))) {
            while (scanner.hasNextLine()) {
                grid.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        int res = 0;
        int[][] coords = {
                {-1, -1}, {-1, 0}, {1, -1},
                {0, -1},          {0, 1},
                {-1, 1}, {1, 0}, {1, 1}
        };
        int rowSize = grid.size();
        int colSize = grid.get(0).length();

        for (int r = 0; r < rowSize; r++) {
            for (int c = 0; c < colSize; c++) {
                if (grid.get(r).charAt(c) == 'X') {
                    for (int[] coord: coords) {
                        int _r = r + coord[0];
                        int _c = c + coord[1];
                        if (isValid(_r, _c, rowSize, colSize) && grid.get(_r).charAt(_c) == 'M') {
                            _r += coord[0];
                            _c += coord[1];
                            if (isValid(_r, _c, rowSize, colSize) && grid.get(_r).charAt(_c) == 'A') {
                                _r += coord[0];
                                _c += coord[1];
                                if (isValid(_r, _c, rowSize, colSize) && grid.get(_r).charAt(_c) == 'S') {
                                    res++;
                                }
                            }
                        }
                    }
                }
            }
        }

        System.out.println("Result for part 1 is: " + res);
    }

    private static boolean isValid(int r, int c, int rowSize, int colSize) {
        return 0 <= r && r < rowSize && 0 <= c && c < colSize;
    }
}
