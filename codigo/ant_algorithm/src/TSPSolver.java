import java.util.ArrayList;
import java.util.Map;

/**
 * TSP algorithm solver interface, useful for passing any of the implemented
 * classes as arguments to other methods
 **/
public interface TSPSolver {
    int[] solve();
}
