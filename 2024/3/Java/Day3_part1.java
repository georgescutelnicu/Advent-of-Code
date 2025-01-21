import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Day3_part1 {
    public static void main(String[] args) {

        String inp = "";
        int res = 0;

        try (Scanner scanner = new Scanner(new File("3.txt"))) {
            while (scanner.hasNextLine()) {
                inp += scanner.nextLine();
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        Pattern pattern = Pattern.compile("mul\\(\\d{1,3},\\d{1,3}\\)");
        Matcher matcher = pattern.matcher(inp);

        while (matcher.find()) {
            String match = matcher.group();
            String[] nums = match.substring(4, match.length() - 1).split(",");

            int x = Integer.valueOf(nums[0]);
            int y = Integer.valueOf(nums[1]);

            res += x * y;
        }

        System.out.println("Result for part 1 is: " + res);
    }
}
