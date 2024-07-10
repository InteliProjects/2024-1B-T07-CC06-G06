//import java.util.Arrays;
//import java.util.HashMap;
//import java.util.Map;
//public class TSPSolverFactory {
//    TSPSolver selectedAlgorithm;
//    public TSPSolverFactory(String type, Map<String, Object> parameters, CSVParser parser) {
//        switch (type.toLowerCase()) {
//            case "antcolony":
//                AntColonyOptimization aco = new AntColonyOptimization();
//                aco.setup(parameters, parser);
//                selectedAlgorithm = aco;
//            default:
//                throw new IllegalArgumentException("Unknown algorithm type: " + type);
//        }
//    }
//
//    public TSPSolver getTSPSolver() {
//        return selectedAlgorithm;
//    }
//
//    public static void main(String[] args) {
//        Map<String, Object> parameters = new HashMap<>();
//        parameters.put("distanceMatrix", new double[][]{{0, 1}, {1, 0}});
//        parameters.put("antNumber", 100);
//        parameters.put("evaporationRate", 0.5);
//        parameters.put("pheromoneInfluence", 1.0);
//        parameters.put("distanceInfluence", 2.0);
//        CSVParser parser = new CSVParser("../../../dataset/AMOSTRA_TOTAL.csv");
//
//        TSPSolverFactory algorithmSelector = new TSPSolverFactory("antcolony",
//                parameters,
//                parser);
//
//        int[] path = algorithmSelector.getTSPSolver().solve();
//        System.out.println(algorithmSelector.getTSPSolver().tourLength(path));
//        System.out.println(Arrays.toString(path));
//    }
//}
