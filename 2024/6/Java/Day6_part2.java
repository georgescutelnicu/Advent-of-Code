import java.io.*;
import java.util.*;

public class Day6_part2 {
    public static void main(String[] args) {

        ArrayList<char[]> grid = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("6.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                grid.add(line.toCharArray());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        int[] guard = findGuard(grid);
        int loops = 0;

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(0).length; c++) {
                if (grid.get(r)[c] == '.') {
                    grid.get(r)[c] = '#';
                    if (isALoop(grid, guard)) {
                        loops++;
                    }
                    grid.get(r)[c] = '.';
                }
            }
        }

        System.out.println("Result for part 2 is: " + loops);
    }

    private static boolean isALoop(ArrayList<char[]> grid, int[] guard) {
        int[][] coords = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int direction = 0;
        Set<String> visited = new HashSet<>();

        while (true) {
            visited.add(guard[0] + "," + guard[1] + "," + coords[direction][0] + "," + coords[direction][1]);
            int r = guard[0], c = guard[1];
            int _r = r + coords[direction][0], _c = c + coords[direction][1];
            if (stillInGrid(_r, _c, grid)) {
                while (grid.get(_r)[_c] == '#') {
                    direction = direction == 3 ? 0 : direction + 1;
                    _r = r + coords[direction][0];
                    _c = c + coords[direction][1];
                }
                guard = new int[]{_r, _c};
                if (visited.contains(guard[0] + "," + guard[1] + "," +
                        coords[direction][0] + "," + coords[direction][1])) {
                    return true;
                }
            } else {
                return false;
            }
        }
    }

    private static int[] findGuard(ArrayList<char[]> grid) {
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(r).length; c++) {
                if (grid.get(r)[c] == '^') {
                    return new int[]{r, c};
                }
            }
        }
        throw new IllegalArgumentException("Guard not found in grid");
    }

    public static boolean stillInGrid(int r, int c, ArrayList<char[]> grid) {
        return 0 <= r && r < grid.size() && 0 <= c && c < grid.get(r).length;
    }
}
