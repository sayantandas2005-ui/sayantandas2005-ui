import java.util.List;

public class java_demo {
    static class DatasetSummary {
        private final List<Double> values;

        DatasetSummary(List<Double> values) {
            this.values = values;
        }

        double mean() {
            return values.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        }
    }

    public static void main(String[] args) {
        DatasetSummary summary = new DatasetSummary(List.of(2.0, 4.0, 6.0, 8.0));
        System.out.printf("Mean: %.2f%n", summary.mean());
    }
}
