import java.io.*;
import java.util.*;

public class Day10_part1 {
    public static void main(String[] args) {

        List<String> grid = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("10.txt"))) {
            while (scanner.hasNextLine()) {
                grid.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        List<int[]> startingPoints = new ArrayList<>();
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(r).length(); c++) {
                if (grid.get(r).charAt(c) == '0') {
                    startingPoints.add(new int[]{r, c});
                }
            }
        }

        int[][] coords = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int res = 0;

        for (int[] start : startingPoints) {
            int startR = start[0], startC = start[1];
            Queue<int[]> q = new ArrayDeque<>();
            Set<String> seen = new HashSet<>();

            q.add(new int[]{startR, startC});
            seen.add(startR + "," + startC);

            while (!q.isEmpty()) {
                int[] current = q.poll();
                int r = current[0], c = current[1];

                for (int[] coord : coords) {
                    int newR = r + coord[0];
                    int newC = c + coord[1];

                    if (stillInGrid(newR, newC, grid) && !seen.contains(newR + "," + newC)) {
                        if (grid.get(newR).charAt(newC) == (char) (grid.get(r).charAt(c) + 1)) {
                            seen.add(newR + "," + newC);

                            if (grid.get(newR).charAt(newC) == '9') {
                                res++;
                            } else {
                                q.add(new int[]{newR, newC});
                            }
                        }
                    }
                }
            }
        }

        System.out.println("Result for part 1 is: " + res);
    }

    private static boolean stillInGrid(int r, int c, List<String> grid) {
        return 0 <= r && r < grid.size() && 0 <= c && c < grid.get(r).length();
    }
}
