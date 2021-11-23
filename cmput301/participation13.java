import java.awt.Point;

public interface RectangleDrawer {
    public void draw( Point topLeft, Point bottomRight );
}

public class RectangleRenderer {
    public void render( int x, int y, int width, int height ) {

    }
}

public class RectangleDrawerAdapter implements RectangleDrawer {
    private RectangleRenderer rectangleRenderer;

    public RectangleDrawerAdapter(RectangleRenderer rectangleRenderer) {
        this.rectangleRenderer = rectangleRenderer;
    }

    public void draw(Point topLeft, Point bottomRight) {
        int x = topLeft.getX();
        int y = topLeft.getY();
        int a = bottomRight.getX();
        int b = bottomRight.getY();

        rectangleRenderer.render( Math.min(x, a), Math.min(y, b), Math.abs(a-x), Math.abs(b-y));
    }
}
