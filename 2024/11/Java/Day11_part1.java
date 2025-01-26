import java.io.*;
import java.util.*;

public class Day11_part1 {
    public static void main(String[] args) {

        List<Long> stones = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("11.txt"))) {
            while (scanner.hasNextInt()) {
                stones.add((long) scanner.nextInt());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        for (int i = 0; i < 25; i++) {
            List<Long> temp = new ArrayList<>();
            for (Long stone : stones) {
                if (stone == 0) {
                    temp.add(1L);
                } else if (String.valueOf(stone).length() % 2 == 0) {
                    int mid = String.valueOf(stone).length() / 2;
                    temp.add(Long.parseLong(String.valueOf(stone).substring(0, mid)));
                    temp.add(Long.parseLong(String.valueOf(stone).substring(mid)));

                } else {
                    temp.add(stone * 2024);
                }
            }
            stones = temp;
        }

        System.out.println("Result for part 1 is: " + stones.size());
    }
}
