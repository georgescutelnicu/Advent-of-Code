import java.io.*;
import java.util.*;
import java.util.concurrent.*;

public class Day11_part2 {

    private static final Map<String, Long> cache = new ConcurrentHashMap<>();

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

        long res = 0;
        for (Long stone : stones) {
            res += countStones(stone, 75);
        }

        System.out.println("Result for part 2 is: " + res);
    }

    private static long countStones(long stone, int iterations) {
        String cacheKey = stone + "," + iterations;
        if (cache.containsKey(cacheKey)) {
            return cache.get(cacheKey);
        }

        if (iterations == 0) {
            return 1;
        }

        long res;

        if (stone == 0) {
            res = countStones(1, iterations - 1);
        } else if (String.valueOf(stone).length() % 2 == 0) {
            int mid = String.valueOf(stone).length() / 2;
            long first = countStones(Long.parseLong(String.valueOf(stone).substring(0, mid)), iterations - 1);
            long second = countStones(Long.parseLong(String.valueOf(stone).substring(mid)), iterations - 1);
            res = first + second;
        } else {
            res = countStones(stone * 2024, iterations - 1);
        }

        cache.put(cacheKey, res);

        return res;
    }
}
// I'm starting to hate Java, Python is much more fun  ❐ ‿ ❑