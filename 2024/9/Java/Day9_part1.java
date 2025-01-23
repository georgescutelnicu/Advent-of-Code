import java.io.*;
import java.util.*;

public class Day9_part1 {
    public static void main(String[] args) {

        StringBuilder inp = new StringBuilder();

        try (Scanner scanner = new Scanner(new File("9.txt"))) {
            while (scanner.hasNextLine()) {
                inp.append(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        System.out.println("Result for part 1 is: " + finalChecksum(moveBlocks(separateBlocks(inp.toString()))));
    }

    private static List<Integer> separateBlocks(String inp) {
        List<Integer> diskMap = new ArrayList<>();
        int count = 0;

        for (int idx = 0; idx < inp.length(); idx++) {
            int value = Character.getNumericValue(inp.charAt(idx));

            if (idx % 2 == 0) {
                for (int i = 0; i < value; i++) {
                    diskMap.add(count);
                }
                count++;
            } else {
                for (int i = 0; i < value; i++) {
                    diskMap.add(null);
                }
            }
        }

        return diskMap;
    }

    private static List<Integer> moveBlocks(List<Integer> inp) {
        int i = 0;
        int j = inp.size() - 1;

        while (i < j) {
            while (inp.get(i) != null) {
                i++;
            }
            while (inp.get(j) == null) {
                j--;
            }

            inp.set(i, inp.get(j));
            inp.set(j, null);
        }

        List<Integer> result = new ArrayList<>();
        for (Integer val : inp) {
            if (val != null) {
                result.add(val);
            }
        }

        return result;
    }

    private static long finalChecksum(List<Integer> inp) {
        long checksum = 0;

        for (int idx = 0; idx < inp.size(); idx++) {
            checksum += (long) idx * inp.get(idx);
        }

        return checksum;
    }
}
