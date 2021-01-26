public class Point {
    int x;
    int y;

    public Point( int startX, int startY ) {
        x = startX;
        y = startY;
    }

    public boolean equals ( Object anotherGuy ) {
        Point another = (Point) anotherGuy;
        return another.x == x && another.y == y;
    }
}
