import java.io.*;
import java.util.*;

public class Day5_part2 {
    public static void main(String[] args) {

        List<String> inp = new ArrayList<>();

        try (Scanner scanner = new Scanner(new File("5.txt"))) {
            while (scanner.hasNextLine()) {
                inp.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        int res = 0;
        List<List<Integer>> updates = new ArrayList<>();
        Map<Integer, List<Integer>> pageOrder = new HashMap<>();

        for (String item : inp) {
            if (item.contains(",")) {
                String[] parts = item.split(",");
                List<Integer> update = new ArrayList<>();
                for (String part : parts) {
                    update.add(Integer.parseInt(part));
                }
                updates.add(update);
            } else if (item.contains("|")) {
                String[] parts = item.split("\\|");
                int key = Integer.parseInt(parts[0]);
                int value = Integer.parseInt(parts[1]);
                if (!pageOrder.containsKey(key)) {
                    pageOrder.put(key, new ArrayList<>());
                }
                pageOrder.get(key).add(value);
            }
        }

        for (List<Integer> update : updates) {
            if (!isCorrectlyOrdered(update, pageOrder)) {
                bubbleSort(update, pageOrder);
                res += update.get(update.size() / 2);
            }
        }

        System.out.println("Result for part 2 is: " + res);
    }

    private static boolean isCorrectlyOrdered(List<Integer> update, Map<Integer, List<Integer>> pageOrder) {
        for (int i = 0; i < update.size() - 1; i++) {
            int currentPage = update.get(i);
            for (int j = i + 1; j < update.size(); j++) {
                int nextPage = update.get(j);
                if (!pageOrder.get(currentPage).contains(nextPage)) {
                    return false;
                }
            }
        }
        return true;
    }

    private static void bubbleSort(List<Integer> update, Map<Integer, List<Integer>> pageOrder) {
        for (int i = update.size() - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                int currentPage = update.get(j);
                int nextPage = update.get(j + 1);
                if (!pageOrder.get(currentPage).contains(nextPage)) {
                    int temp = update.get(j);
                    update.set(j, update.get(j + 1));
                    update.set(j + 1, temp);
                }
            }
        }
    }
}
