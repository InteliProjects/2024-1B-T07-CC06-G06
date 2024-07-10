import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Parses CSV files to extract data from the clusters CSVs, use that information to retrieve
 * the points contained within the cluster in the total sample and finally build a distance matrix,
 * that will be consumed posteriorly by the TSP algorithms.
 */
public class CSVParser {
    String csv_path; // Path to the CSV file containing cluster information.

    /**
     * Constructs a CSVParser object with the specified path to a CSV file.
     *
     * @param csv_path the path to the CSV file that contains cluster indices.
     */
    public CSVParser(String csv_path) {
        this.csv_path = csv_path;
    }

    /**
     * Parses the CSV file specified by csv_path to extract points defined by their coordinates.
     * This method reads indices from a cluster CSV and then fetches corresponding coordinates from a total dataset CSV.
     *
     * @return an ArrayList of Points extracted from the dataset.
     */
    private ArrayList<Point> parse() {
        try (BufferedReader brCluster = new BufferedReader(new FileReader(csv_path))) {
            BufferedReader brTotal = new BufferedReader(new FileReader("../dataset/AMOSTRA_TOTAL.csv"));
            ArrayList<Point> res = new ArrayList<>();
            brCluster.readLine(); // Skip header line

            String line = brCluster.readLine();
            String[] values = line.split(",");
            String[] indicesString = values[1].split(" ");
            int[] indices = new int[indicesString.length];
            for (int i = 0; i < indicesString.length; i++) {
                indices[i] = Integer.parseInt(indicesString[i]);
            }
            Arrays.sort(indices);

            ArrayList<String[]> totalMatrix = new ArrayList<>();
            String totalLine = brTotal.readLine(); // Skip header line
            while ((totalLine = brTotal.readLine()) != null) {
                String[] totalLineArray = totalLine.split(";");
                totalMatrix.add(totalLineArray);
            }
            for (int index : indices) {
                String[] currLine = totalMatrix.get(index);
                res.add(new Point(Double.parseDouble(currLine[1]), Double.parseDouble(currLine[2])));
            }
            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * Generates a distance matrix from the points parsed by the parse method.
     * This matrix is symmetrical and contains the distances between each pair of points.
     *
     * @return a 2D array of doubles representing the distance matrix for the points.
     */
    public double[][] distanceMatrixGenerator() {
        ArrayList<Point> parsed_csv = parse();
        if (parsed_csv == null) {
            return null; // Handle error or empty parse result
        }
        int n = parsed_csv.size();
        double[][] res = new double[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = Point.length(parsed_csv.get(i), parsed_csv.get(j));
            }
        }

        return res;
    }

    public static void main(String[] args) {

    }
}
