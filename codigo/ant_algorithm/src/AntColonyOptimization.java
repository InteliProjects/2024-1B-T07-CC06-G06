import java.util.*;
/**
 * Represents an ant in the Ant Colony Optimization algorithm. This class manages the ant's tour through points,
 * tracking the points it has visited, the current tour's length, and the sequence of points in the tour.
 */
class Ant {
    int[] tour;
    boolean[] visited;
    int tourIndex;
    double[][] distanceMatrix;
    double tourLength;

    /**
     * Constructs an Ant with a specified number of points and a reference to the shared distance matrix.
     * @param numberOfPoints the number of points in the problem
     * @param distanceMatrix the distance matrix representing the distances between each pair of points
     */
    public Ant(int numberOfPoints, double[][] distanceMatrix) {
        tour = new int[numberOfPoints];
        visited = new boolean[numberOfPoints];
        this.distanceMatrix = distanceMatrix;
    }

    /**
     * Marks a point as visited by this ant and updates the tour length.
     * @param point the index of the point to visit
     */
    void visitPoint(int point) {
        tour[tourIndex++] = point;
        visited[point] = true;
        if (tourIndex > 1) {
            tourLength += distanceMatrix[tour[tourIndex - 2]][point];
        }
    }

    /**
     * Checks if a point has already been visited by this ant.
     * @param point the index of the point to check
     * @return true if the point has been visited, false otherwise
     */
    boolean visited(int point) {
        return visited[point];
    }

    /**
     * Returns the index of the current point in which the ant is located.
     * @return the current point index
     */
    int currentPoint() {
        return tour[tourIndex - 1];
    }

    /**
     * Returns the total length of the current tour.
     * @return the length of the tour
     */
    public double tourLength() {
        return tourLength;
    }

    /**
     * Resets the ant's state for a new tour.
     */
    void clear() {
        Arrays.fill(visited, false);
        tourLength = 0;
        tourIndex = 0;
    }
}

/**
 * Implements the Ant Colony Optimization algorithm for solving the traveling salesman problem.
 * Manages the simulation of a colony of ants exploring paths through points to find the shortest possible tour.
 */
public class AntColonyOptimization implements TSPSolver{
    private double[][] pheromoneMatrix;
    private double[][] distanceMatrix;
    private Ant[] ants;
    private int antNumber;
    private int iterations;
    private int numberOfPoints;
    private double evaporationRate;
    private double pheromoneInfluence;
    private double distanceInfluence;

    /**
     * Constructs an instance of the Ant Colony Optimization algorithm.
     * @param distanceMatrix matrix representing the distances between points
     * @param antNumber number of ants to simulate
     * @param evaporationRate rate at which pheromone trails evaporate
     * @param pheromoneInfluence degree to which pheromones influence ant decisions
     * @param distanceInfluence degree to which point distances influence ant decisions
     * @param iterations number of iterations to run the simulation
     */
    public AntColonyOptimization(
            double[][] distanceMatrix,
            int antNumber,
            double evaporationRate,
            double pheromoneInfluence,
            double distanceInfluence,
            int iterations) {

        this.numberOfPoints =   distanceMatrix.length;
        pheromoneMatrix = new double[numberOfPoints][numberOfPoints];
        this.distanceMatrix = distanceMatrix;
        this.antNumber = antNumber;
        this.evaporationRate = evaporationRate;
        this.pheromoneInfluence = pheromoneInfluence;
        this.distanceInfluence = distanceInfluence;
        this.iterations = iterations;
        for (double[] row : pheromoneMatrix) {
            Arrays.fill(row, 1.0);
        }
        ants = new Ant[antNumber];
        for (int i = 0; i < antNumber; i++) {
            ants[i] = new Ant(numberOfPoints, distanceMatrix);
        }
    }

    /**
     * Prepares ants for a new simulation round by resetting their state and placing each at a random starting point.
     */
    private void setup() {
        for (Ant a: ants) {
            a.clear();
            a.visitPoint((int) (Math.random() * numberOfPoints));
        }
    }

    /**
     * Calculates the desirability of moving from one point to another based on the pheromone level and distance.
     * @param i the starting point index
     * @param j the destination point index
     * @return the calculated desire value
     */
    private double desire(int i, int j) {
        return Math.pow(pheromoneMatrix[i][j], pheromoneInfluence) *
                Math.pow(1/distanceMatrix[i][j], distanceInfluence);
    }

    /**
     * Simulates the movement of all ants for one iteration.
     */
    private void simulateAnts() {
        for (int i = 0; i < numberOfPoints - 1; i++) {
            for (Ant ant : ants) {
                int nextPoint = selectNextPoint(ant);
                ant.visitPoint(nextPoint);
            }
        }
    }

    /**
     * Updates the pheromone levels on all paths based on the tours completed by the ants.
     */
    private void updatePheromones() {
        for (double[] row : pheromoneMatrix) {
            for (int i = 0; i < row.length; i++) {
                row[i] *= (1 - evaporationRate);
            }
        }
        for (Ant ant : ants) {
            double contribution = 1.0 / ant.tourLength();
            for (int i = 0; i < ant.tourLength; i++) {
                int pointX = ant.tour[i];
                int pointY = ant.tour[i + 1];
                pheromoneMatrix[pointX][pointY] += contribution;
                pheromoneMatrix[pointY][pointX] += contribution;
            }
        }
    }

    /**
     * Selects the next point for an ant to visit based on the calculated desirability of each possible move.
     * @param ant the ant making the move
     * @return the index of the next point to visit
     */
    private int selectNextPoint(Ant ant) {
        int currentPoint = ant.currentPoint();
        double[] probabilities = new double[numberOfPoints];
        double probabilitySum = 0;

        for (int i = 0; i < numberOfPoints; i++) {
            if (!ant.visited(i)) {
                probabilities[i] = desire(currentPoint, i);
                probabilitySum += probabilities[i];
            }
        }

        double random = Math.random() * probabilitySum;
        double cumulativeProbability = 0.0;
        for (int i = 0; i < numberOfPoints; i++) {
            if (!ant.visited(i)) {
                cumulativeProbability += probabilities[i];
                if (cumulativeProbability >= random) {
                    return i;
                }
            }
        }

        throw new RuntimeException("No available point found - this should never happen!");
    }


    /**
     * Calculates the total length of a given tour.
     * @param tour the complete tour made by an ant
     * @return total length
     **/
    private double calculateTourLength(int[] tour) {
        double length = 0.0;
        for (int i = 0; i < tour.length - 1; i++) {
            length += distanceMatrix[tour[i]][tour[i + 1]];
        }
        return length;
    }

    /**
     * Solves the traveling salesman problem using the ant colony optimization algorithm.
     * @return the best tour found after all iterations
     */
    public int[] solve() {
        int[] globalBestTour = null;
        double globalBestLength = Double.MAX_VALUE;
        for (int i = 0; i < iterations; i++) {
            System.out.println(i);
            setup();
            simulateAnts();
            updatePheromones();
            int[] localBestTour = getBestTour();
            double localBestLength = calculateTourLength(localBestTour);
            if (localBestLength < globalBestLength) {
                globalBestTour = localBestTour;
                globalBestLength = localBestLength;
            }
        }
        return globalBestTour;
    }

    /**
     * Finds the best tour from the current set of ants.
     * @return the best tour as an array of point indices
     */
    private int[] getBestTour() {
        double bestLength = Double.MAX_VALUE;
        int[] bestTour = null;
        for (Ant ant : ants) {
            if (ant.tourLength() < bestLength) {
                bestLength = ant.tourLength();
                bestTour = ant.tour.clone();
            }
        }
        return bestTour;
    }

    public static void main(String[] args) {
        CSVParser parser = new CSVParser("../greedy-algorithm/ResultadosGreedy/cluster_0.csv");
        double[][] distanceMatrix = parser.distanceMatrixGenerator();
        AntColonyOptimization aco = new AntColonyOptimization(distanceMatrix, 1000,
                0.1,
                1.22,
                2.3,
                1000);

        int[] tour = aco.solve();
        aco.calculateTourLength(tour);
    }
}