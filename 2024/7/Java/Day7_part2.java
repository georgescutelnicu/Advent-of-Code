import java.io.*;
import java.util.*;

public class Day7_part2 {
    public static void main(String[] args) {

        List<Long> targets = new ArrayList<>();
        List<List<Long>> numbers = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("7.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(":");

                targets.add(Long.parseLong(parts[0]));

                List<Long> nums = new ArrayList<>();
                for (String num : parts[1].trim().split("\\s+")) {
                    nums.add(Long.parseLong(num));
                }
                numbers.add(nums);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        long res = 0;

        for (int i = 0; i < numbers.size(); i++) {
            long target = targets.get(i);
            List<Long> nums = numbers.get(i);
            if (isAMatch(target, nums, nums.get(0), 1)) {
                res += target;
            }
        }

        System.out.println("Result for part 2 is: " + res);
    }

    private static boolean isAMatch(long target, List<Long> nums, long total, int idx) {
        if (idx == nums.size()) {
            return target == total;
        }

        return isAMatch(target, nums, total + nums.get(idx), idx + 1) ||
                isAMatch(target, nums, total * nums.get(idx), idx + 1) ||
                isAMatch(target, nums, Long.parseLong(String.valueOf(total) + nums.get(idx)), idx + 1);
    }
}
