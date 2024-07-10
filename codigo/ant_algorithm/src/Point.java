/**
 * Represents a point in a two-dimensional space with x and y coordinates.
 */
public class Point {
    public double x;
    public double y;

    /**
     * Constructs a new point with the specified x and y coordinates.
     *
     * @param x the x-coordinate of the new point
     * @param y the y-coordinate of the new point
     */
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Calculates and returns the Euclidean distance between two points.
     *
     * @param p1 the first point
     * @param p2 the second point
     * @return the distance between points p1 and p2
     */
    public static double length(Point p1, Point p2) {
        return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
    }
}
