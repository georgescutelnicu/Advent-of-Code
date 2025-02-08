import java.io.*;
import java.util.*;

public class Day13_part1 {

    public static void main(String[] args) {
        StringBuilder inp = new StringBuilder();

        try (Scanner scanner = new Scanner(new File("13.txt"))) {
            while (scanner.hasNextLine()) {
                inp.append(scanner.nextLine()).append("\n");
            }
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
            return;
        }

        List<int[]> numbers = extractNumbers(inp.toString());
        int aPrice = 3, bPrice = 1, res = 0;

        for (int[] vals : numbers) {
            int aX = vals[0], aY = vals[1], bX = vals[2], bY = vals[3], pX = vals[4], pY = vals[5];
            int minTokens = Integer.MAX_VALUE;

            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    if (aX * i + bX * j == pX && aY * i + bY * j == pY) {
                        minTokens = Math.min(minTokens, i * aPrice + j * bPrice);
                    }
                }
            }
            res += (minTokens == Integer.MAX_VALUE) ? 0 : minTokens;
        }

        System.out.println("Result for part 1 is: " + res);
    }

    private static List<int[]> extractNumbers(String inp) {
        List<int[]> numbers = new ArrayList<>();
        String[] machines = inp.split("\n\n");
        StringBuilder num = new StringBuilder();

        for (String machine : machines) {
            List<Integer> machineNum = new ArrayList<>();

            for (char ch : machine.toCharArray()) {
                if (Character.isDigit(ch)) {
                    num.append(ch);
                } else if (num.length() > 0) {
                    machineNum.add(Integer.parseInt(num.toString()));
                    num.setLength(0);
                }
            }
            if (num.length() > 0) {
                machineNum.add(Integer.parseInt(num.toString()));
                num.setLength(0);
            }
            int[] arr = new int[machineNum.size()];
            for (int i = 0; i < machineNum.size(); i++) {
                arr[i] = machineNum.get(i);
            }
            numbers.add(arr);
        }
        return numbers;
    }
}
