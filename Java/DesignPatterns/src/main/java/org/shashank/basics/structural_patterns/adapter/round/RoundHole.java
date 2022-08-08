package org.shashank.basics.structural_patterns.adapter.round;

public class RoundHole {
    private double radius;

    public RoundHole(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public boolean fits(CylindericalObject obj) {
        boolean result;
        result = (this.getRadius() >= obj.getRadius());
        return result;
    }
}