import java.io.*;
import java.util.*;

public class Day1 {
    public static void main(String[] args) {

        List<Integer> nums1 = new ArrayList<>();
        List<Integer> nums2 = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("1.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split("\\s+");
                nums1.add(Integer.parseInt(parts[0]));
                nums2.add(Integer.parseInt(parts[1]));
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        Collections.sort(nums1);
        Collections.sort(nums2);

        int res1 = 0;
        int res2 = 0;

        for (int i = 0; i < nums1.size(); i++) {
            res1 += Math.abs(nums1.get(i) - nums2.get(i));
        }

        for (int num : nums1) {
            int count = Collections.frequency(nums2, num);
            res2 += num * count;
        }

        System.out.println("Result for part 1 is: " + res1);
        System.out.println("Result for part 2 is: " + res2);
    }
}
