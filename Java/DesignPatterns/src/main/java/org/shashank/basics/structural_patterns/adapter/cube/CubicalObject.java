package org.shashank.basics.structural_patterns.adapter.cube;

public class CubicalObject {
    private final double width;

    public CubicalObject(double width) {
        this.width = width;
    }

    public double getWidth() {
        return width;
    }

    public double getSquare() {
        double result;
        result = Math.pow(this.width, 2);
        return result;
    }

}
