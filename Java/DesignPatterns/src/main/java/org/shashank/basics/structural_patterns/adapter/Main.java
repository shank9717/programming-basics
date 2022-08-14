package org.shashank.basics.structural_patterns.adapter;

import org.shashank.basics.structural_patterns.adapter.adapters.CubeToCylinderAdapter;
import org.shashank.basics.structural_patterns.adapter.cube.CubicalObject;
import org.shashank.basics.structural_patterns.adapter.round.CylindericalObject;
import org.shashank.basics.structural_patterns.adapter.round.RoundHole;

public class Main {
    public static void main(String[] args) {
        RoundHole hole = new RoundHole(5);
        CylindericalObject cylinder = new CylindericalObject(5);
        if (hole.fits(cylinder)) {
            System.out.println("Cylinder is exact fit in round hole");
        }

        CubicalObject smallCube = new CubicalObject(2);
        CubicalObject largeCube = new CubicalObject(20);
        // hole.fits(smallCube); // Won't compile.

        CubeToCylinderAdapter smallCubeAdapter = new CubeToCylinderAdapter(smallCube);
        CubeToCylinderAdapter largeCubeAdapter = new CubeToCylinderAdapter(largeCube);
        if (hole.fits(smallCubeAdapter)) {
            System.out.println("Small cube fits the round hole");
        }
        if (!hole.fits(largeCubeAdapter)) {
            System.out.println("Big cube doesn't fit the round hole");
        }
    }
}
