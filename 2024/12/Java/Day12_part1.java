import java.io.*;
import java.util.*;

public class Day12_part1 {

    public static void main(String[] args) {
        List<String> grid = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("12.txt"))) {
            while (scanner.hasNextLine()) {
                grid.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        int[][] coords = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        List<Set<String>> regions = new ArrayList<>();
        Set<String> seen = new HashSet<>();
        int res = 0;

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(r).length(); c++) {
                if (!seen.contains( r + "," + c)) {
                    seen.add( r + "," + c);
                    ArrayDeque<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{r, c});
                    Set<String> region = new HashSet<>();
                    region.add( r + "," + c);

                    while (!q.isEmpty()) {
                        int[] curr = q.poll();
                        int currR = curr[0], currC = curr[1];

                        for (int[] coord : coords) {
                            int _r = currR + coord[0], _c = currC + coord[1];

                            if (stillInGrid(_r, _c, grid) && !region.contains(_r + "," + _c) &&
                                    grid.get(_r).charAt(_c) == grid.get(currR).charAt(currC)) {
                                region.add(_r + "," + _c);
                                q.add(new int[]{_r, _c});
                                seen.add(_r + "," + _c);
                            }
                        }
                    }

                    regions.add(region);
                }
            }
        }

        for (Set<String> region : regions) {
            int perimeter = 0;
            for (String cell : region) {
                String[] parts = cell.split(",");
                int rCell = Integer.parseInt(parts[0]), cCell = Integer.parseInt(parts[1]);
                int neighbors = 0;

                for (int[] coord : coords) {
                    int _r = rCell + coord[0], _c = cCell + coord[1];
                    if (region.contains(_r + "," + _c)) {
                        neighbors++;
                    }
                }
                perimeter += 4 - neighbors;
            }
            res += perimeter * region.size();
        }

        System.out.println("Result for part 1 is: " + res);
    }

    private static boolean stillInGrid(int r, int c, List<String> grid) {
        return 0 <= r && r < grid.size() && 0 <= c && c < grid.get(r).length();
    }
}
