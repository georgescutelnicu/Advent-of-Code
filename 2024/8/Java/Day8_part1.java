import java.io.*;
import java.util.*;

public class Day8_part1 {
    public static void main(String[] args) {

        List<String> grid = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("8.txt"))) {
            while (scanner.hasNextLine()) {
                grid.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        Map<Character, List<int[]>> antennas = new HashMap<>();
        Set<String> antinodes = new HashSet<>();

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid.get(r).length(); c++) {
                char current = grid.get(r).charAt(c);
                if (current != '.') {
                    antennas.putIfAbsent(current, new ArrayList<>());
                    antennas.get(current).add(new int[]{r, c});
                }
            }
        }

        for (Character antenna : antennas.keySet()) {
            List<int[]> locations = antennas.get(antenna);

            for (int i = 0; i < locations.size(); i++) {
                for (int j = 0; j < locations.size(); j++) {
                    if (i == j) continue;

                    int[] loc1 = locations.get(i);
                    int[] loc2 = locations.get(j);

                    int[] antinode = antinodeOffset(loc1[0], loc1[1], loc2[0], loc2[1]);

                    if (stillInGrid(antinode[0], antinode[1], grid)) {
                        antinodes.add(antinode[0] + "," + antinode[1]);
                    }
                }
            }
        }

        System.out.println("Result for part 1 is: " + antinodes.size());
    }

    private static boolean stillInGrid(int r, int c, List<String> grid) {
        return 0 <= r && r < grid.size() && 0 <= c && c < grid.get(r).length();
    }

    private static int[] antinodeOffset(int r1, int c1, int r2, int c2) {
        int rDiff = Math.abs(r1 - r2);
        int cDiff = Math.abs(c1 - c2);

        int rAn = (r1 < r2) ? r1 - rDiff : r1 + rDiff;
        int cAn = (c1 < c2) ? c1 - cDiff : c1 + cDiff;

        return new int[]{rAn, cAn};
    }
}
