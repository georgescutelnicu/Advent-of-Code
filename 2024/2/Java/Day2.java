import java.io.*;
import java.util.*;

public class Day2 {
    public static void main(String[] args) {

        List<List<Integer>> reports = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("2.txt"))) {
            while (scanner.hasNextLine()) {
                String[] parts = scanner.nextLine().split(" ");
                List<Integer> report = new ArrayList<>();
                for (String part: parts) {
                    report.add(Integer.valueOf(part));
                }
                reports.add(report);
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        int safeReports = 0;
        int safeReports2 = 0;

        for (List<Integer> report: reports) {
            if (is_safe(report)) {
                safeReports++;
            }
        }

        for (List<Integer> report: reports) {
            for (int i = 0; i < report.size(); i++) {
                List<Integer> modifiedReport = new ArrayList<>(report.subList(0, i));
                modifiedReport.addAll(report.subList(i + 1, report.size()));
                if (is_safe(modifiedReport)) {
                    safeReports2++;
                    break;
                }
            }
        }

        System.out.println("Result for part 1 is: " + safeReports);
        System.out.println("Result for part 2 is: " + safeReports2);
    }

    public static boolean is_safe(List<Integer> l) {

        if (l.get(0) < l.get(1)) {
            for (int i = 1; i < l.size(); i++) {
                if ((l.get(i) - l.get(i - 1) < 1) || (l.get(i) - l.get(i-1) > 3)) {
                    return false;
                }
            }
        } else {
            for (int i = 1; i < l.size(); i++) {
                if ((l.get(i - 1) - l.get(i) < 1) || (l.get(i - 1) - l.get(i) > 3)) {
                    return false;
                }
            }
        }
        return true;
    }
}
