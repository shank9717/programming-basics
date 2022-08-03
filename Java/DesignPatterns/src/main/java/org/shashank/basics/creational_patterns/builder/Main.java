/*
Unlike other creational patterns, Builder doesn’t require products to have a common interface.
That makes it possible to produce different products using the same construction process.
The Builder pattern can be recognized in a class, which has a single creation method
and several methods to configure the resulting object. Builder methods often support chaining
 */
package org.shashank.basics.creational_patterns.builder;

import org.shashank.basics.creational_patterns.builder.builders.RobotBuilder;
import org.shashank.basics.creational_patterns.builder.director.RobotBuildingDirector;
import org.shashank.basics.creational_patterns.builder.robots.Robot;

public class Main {
    public static void main(String[] args) {
        RobotBuildingDirector director = new RobotBuildingDirector();

        RobotBuilder builder = new RobotBuilder();
        director.createHumanoidRobot(builder);

        Robot robot = builder.get();
        System.out.println("Robot built of type: " + robot.getType());
        System.out.println("It has " + robot.getSensorCount() + " sensors");
    }
}
