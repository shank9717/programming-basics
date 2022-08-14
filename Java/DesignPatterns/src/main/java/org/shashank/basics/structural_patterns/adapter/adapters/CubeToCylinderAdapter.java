package org.shashank.basics.structural_patterns.adapter.adapters;

import org.shashank.basics.structural_patterns.adapter.cube.CubicalObject;
import org.shashank.basics.structural_patterns.adapter.round.CylindericalObject;

public class CubeToCylinderAdapter extends CylindericalObject {

    private final CubicalObject object;

    public CubeToCylinderAdapter(CubicalObject object) {
        this.object = object;
    }

    @Override
    public double getRadius() {
        return (Math.sqrt(Math.pow((object.getWidth() / 2), 2) * 2));
    }
}
